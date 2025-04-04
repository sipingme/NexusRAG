import langchain
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.agents.rag_agent import RAGAgent
from app.llms.llm_manager import LLMManager
from app.prompts.agent_prompt import AgentPrompt
from app.prompts.answer_prompt import AnswerPrompt
from app.prompts.optimize_prompt import OptimizePrompt
from app.stores.vector_storage import VectorStorage

class QAChain:
    def __init__(self):
        langchain.debug = False

        self.vector_db = VectorStorage.create_storage("chroma")
        self.retriever = self.vector_db.as_retriever()
        self.llm = LLMManager.create_llm("openai").initialize()

        self.agent_prompt = AgentPrompt().from_messages()
        self.answer_prompt = AnswerPrompt().from_template()
        self.optimize_prompt = OptimizePrompt().from_template()
        self.agent = RAGAgent(self.llm, self.retriever, self.agent_prompt, self.answer_prompt).execute()

    def executor(self, question):
        qa_pipeline = (
            RunnableParallel(
                question=RunnablePassthrough(),
                context=lambda x: self.retriever.invoke(x["query"])
            )
            | self._optimization_stage()
            | self._processing_stage()
        )
        result = qa_pipeline.invoke({
            "query": question
        })
        return result
    
    def _optimization_stage(self):
        return RunnableParallel(
            optimized_question=RunnablePassthrough.assign(
                question=lambda x: x["question"],
                context=lambda x: x["context"]
            )
            | self.optimize_prompt
            | self.llm
            | StrOutputParser()
        )
    
    def _processing_stage(self):
        return RunnableParallel(
            agent_result=lambda x: self.agent.invoke(
                {"input": x["optimized_question"]}
            ),
            # .with_retry(stop=3)
            rag_result=RunnablePassthrough.assign(
                question=lambda x: x["optimized_question"],
                context=lambda x: self.retriever.invoke(x["optimized_question"])
            )
            | self.answer_prompt
            | self.llm
            | StrOutputParser()
        )
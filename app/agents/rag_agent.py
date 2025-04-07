from langchain.agents import AgentExecutor, create_tool_calling_agent
from app.tools.tool_registry import ToolRegistry
class RAGAgent:
    def __init__(self, llm, retriever, agent_prompt, answer_prompt):
        self.tools = ToolRegistry().create_tools(llm, retriever, answer_prompt)
        self.agent = create_tool_calling_agent(llm, self.tools, agent_prompt)

    def execute(self):
        agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            return_intermediate_steps=True,
            verbose=True
        )
        return agent_executor
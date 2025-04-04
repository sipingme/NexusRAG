from langchain.tools import Tool
class AnnualScoreTool:
    def __init__(self, llm, retriever, answer_prompt):
        self.llm = llm
        self.answer_prompt = answer_prompt
        self.retriever = retriever

    def initialize(self):
        return Tool(
            name="AnnualScoreTool",
            func=self.annual_score_wrapper,
            description=(
                "该工具旨在查询并提供全面的大学录取分数线信息。"
                "它提供每个专业的具体分数线，包括不同录取批次和要求的变化。"
                "用户可以利用此工具获取最新且准确的分数数据，以帮助做出有关大学申请的明智决策。"
            )
        )
    
    def annual_score_wrapper(self, input_text):
        _content = ""
        context = self.retriever.invoke(input_text)
        for i in context:
            _content += i.page_content
        messages = self.answer_prompt.format_messages(
            context=_content,
            question=input_text
        )
        results = self.llm.invoke(messages)
        return results
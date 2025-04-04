from langchain.tools import Tool
class MajorPlanTool:
    def __init__(self, llm, retriever, answer_prompt):
        self.llm = llm
        self.answer_prompt = answer_prompt
        self.retriever = retriever
    
    def initialize(self):
        return Tool(
            name="MajorPlanTool",
            func=self.major_plan_wrapper,
            description=(
                "该工具用于检索大学的招生计划和学院的专业设置。"
                "它提供详细的专业信息，帮助用户了解具体专业的课程安排、入学要求和其他相关内容。"
                "用户可以利用此工具获取全面的专业设置信息，以支持教育规划和决策。"
            )
        )
    
    def major_plan_wrapper(self, input_text):
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
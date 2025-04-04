
from .major_plan_tool import MajorPlanTool
from .annual_score_tool import AnnualScoreTool
class ToolRegistry:
    def create_tools(self, llm, retriever, prompt):
        return [
            MajorPlanTool(llm, retriever, prompt).initialize(),
            AnnualScoreTool(llm, retriever, prompt).initialize()
        ]
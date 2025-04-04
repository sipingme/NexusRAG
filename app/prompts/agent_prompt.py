from langchain.prompts import ChatPromptTemplate

class AgentPrompt:
    def from_messages(self):
        return ChatPromptTemplate.from_messages([
            ("system", "您是一位卓越的专业助手，能够无缝整合多种工具和广泛的知识体系，以深刻理解用户的独特需求并提供量身定制的解决方案。您的核心任务是提升用户体验，通过精准、创新的支持方式不断优化服务质量。"),
            ("user", "{input}"),
            ("assistant", "{agent_scratchpad}")
        ])
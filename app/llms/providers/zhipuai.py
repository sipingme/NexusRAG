from langchain_community.chat_models import ChatZhipuAI

class ZHIPUAI:
    def initialize(self):
       return ChatZhipuAI(
            temperature=0
        )
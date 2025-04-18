from langchain_community.chat_models import ChatZhipuAI
from app.config import Settings

settings = Settings()

class ZHIPUAI:
    def __init__(self):
        self.api_key = settings.zhipuai_api_key
        self.api_base = settings.zhipuai_api_base
        self.model = settings.zhipuai_api_model
        self.temperature = settings.temperature
        self.chat_model = self._initialize_chat_model()

    def _initialize_chat_model(self):
        try:
            return ChatZhipuAI(
                api_key=self.api_key,
                api_base=self.api_base,
                model=self.model,
                temperature=self.temperature
            )
        except Exception as e:
            raise RuntimeError(f"初始化 ChatZhipuAI 模型失败: {e}")

    def get_chat_model(self):
        return self.chat_model
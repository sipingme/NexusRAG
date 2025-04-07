from langchain_openai import ChatOpenAI
from app.config import Settings

settings = Settings()

class OPENAI:
    def __init__(self):
        self.api_key = settings.openai_api_key
        self.model = settings.openai_api_model
        self.temperature = settings.temperature
        self.chat_model = self._initialize_chat_model()

    def _initialize_chat_model(self):
        try:
            return ChatOpenAI(
                openai_api_key=self.api_key,
                model_name=self.model,
                temperature=self.temperature
            )
        except Exception as e:
            raise RuntimeError(f"初始化 ChatOpenAI 模型失败: {e}")

    def get_chat_model(self):
        try:
            return ChatOpenAI(
                openai_api_key=self.api_key,
                model_name=self.model,
                temperature=self.temperature
            )
        except Exception as e:
            raise RuntimeError(f"初始化 ChatOpenAI 模型失败: {e}")
from langchain_community.chat_models.tongyi import ChatTongyi
from app.config import Settings

settings = Settings()

class TONGYIQWEN:
    def __init__(self):
        self.api_key = settings.tongyi_api_key
        self.model = settings.tongyi_api_model
        self.temperature = settings.temperature
        self.chat_model = self._initialize_chat_model()

    def _initialize_chat_model(self):
        try:
            return ChatTongyi(
                api_key=self.api_key,
                model=self.model,
                temperature=self.temperature
            )
        except Exception as e:
            raise RuntimeError(f"初始化 ChatTongyi 模型失败: {e}")

    def get_chat_model(self):
        return self.chat_model
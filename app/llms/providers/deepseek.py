from langchain_deepseek import ChatDeepSeek
from app.config import Settings

settings = Settings()

class DEEPSEEK:
    def __init__(self):
        self.api_key = settings.deepseek_api_key
        self.base_url = settings.deepseek_api_base
        self.model = settings.deepseek_api_model
        self.temperature = settings.temperature
        self.chat_model = self._initialize_chat_model()

    def _initialize_chat_model(self):
        try:
            return ChatDeepSeek(
                api_key=self.api_key,
                base_url=self.base_url,
                model=self.model,
                temperature=self.temperature
            )
        except Exception as e:
            raise RuntimeError(f"初始化 ChatDeepSeek 模型失败: {e}")

    def get_chat_model(self):
        return self.chat_model
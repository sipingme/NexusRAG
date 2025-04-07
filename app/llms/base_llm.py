from abc import ABC, abstractmethod
from app.config import Settings

settings = Settings()

class BaseLLM(ABC):
    @abstractmethod
    def initialize(self):
        pass
    
    @abstractmethod
    def get_chat_model(self):
        pass
from abc import ABC, abstractmethod
from .providers.zhipuai import ZHIPUAI
from .providers.openai import OPENAI

class LLMManager(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @classmethod
    def create_llm(cls, llm_type):
        llm_map = {
            "zhipuai": ZHIPUAI,
            "openai": OPENAI
        }
        return llm_map[llm_type]
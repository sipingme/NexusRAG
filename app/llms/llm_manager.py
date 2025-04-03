from abc import ABC, abstractmethod
from .providers.zhipuai import ZHIPUAI

class LLMManager(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @classmethod
    def create_llm(cls, llm_type):
        llm_map = {
            "zhipuai": ZHIPUAI
        }
        return llm_map[llm_type]
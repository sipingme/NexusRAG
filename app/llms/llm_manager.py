from abc import ABC, abstractmethod
from .providers.deepseek import DEEPSEEK
from .providers.openai import OPENAI
from .providers.tongyiqwen import TONGYIQWEN
from .providers.zhipuai import ZHIPUAI
class LLMManager(ABC):
    @abstractmethod
    def initialize(self):
        pass

    @classmethod
    def create_llm(cls, llm_type: str):
        llm_map = {
            "deepseek": DEEPSEEK,
            "openai": OPENAI,
            "tongyiqwen": TONGYIQWEN,
            "zhipuai": ZHIPUAI
        }
        if llm_type not in llm_map:
            raise ValueError(f"不支持的语言模型类型: {llm_type}。支持的类型有: {list(llm_map.keys())}")
        
        return llm_map[llm_type]
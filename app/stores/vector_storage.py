from abc import ABC, abstractmethod
from langchain_community.embeddings import ZhipuAIEmbeddings
from app.config import Settings
from .chroma import ChromaStorage

settings = Settings()

class VectorStorage(ABC):
    @abstractmethod
    def store_documents(self, documents):
        pass

    @abstractmethod
    def similarity_search(self, query, k):
        pass

    @abstractmethod
    def as_retriever():
        pass

    @abstractmethod
    def delete_collection(self) -> bool:
        pass

    @classmethod
    def create_storage(cls, storage_type):
        embedding = ZhipuAIEmbeddings(
            ZHIPUAI_API_KEY=settings.zhipuai_api_key,
            ZHIPUAI_API_BASE=settings.zhipuai_api_base,
            ZHIPUAI_API_MODEL=settings.zhipuai_api_model,
            ZHIPUAI_API_EMBEDDING=settings.zhipuai_api_embedding
        )
        storage_map = {
            "chroma": ChromaStorage
        }
        return storage_map[storage_type](embedding)
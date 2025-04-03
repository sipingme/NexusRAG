# import chromadb
from typing import List
from pathlib import Path
from langchain_chroma import Chroma
from app.config import Settings
from app.logger import initialize_logger

settings = Settings()
logger = initialize_logger(settings.log_level)
class ChromaStorage():
    def __init__(self, embedding):
        # self.client = chromadb.HttpClient(
        #     host=settings.vector_db_host,
        #     port=settings.vector_db_port,
        #     settings=chromadb.Settings(allow_reset=True)
        # )
        path = Path(settings.vector_store_path)
        self.vector_store = Chroma(
            collection_name=settings.nexus_rag_collection,
            embedding_function=embedding,
            persist_directory=str(path)
        )

    def store_documents(self, documents) -> List[str]:
        try:
            self.vector_store.add_documents(documents)
            return True
        except Exception as e:
            logger.error(f"Chroma存储文档失败: {str(e)}")
            return False

    def as_retriever(self):
        return self.vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={"score_threshold":.1, "k":1}
        )

    def similarity_search(self, query: str, k: int = 5):
        return self.vector_store.similarity_search(query, k=k)

    # def delete_collection(self) -> bool:
    #     try:
    #         self.client.delete_collection(settings.nexus_rag_collection)
    #         return True
    #     except Exception as e:
    #         logger.error(f"删除Chroma集合失败: {str(e)}")
    #         return False
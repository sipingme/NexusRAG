import os
from typing import Optional
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config import Settings
from app.logger import initialize_logger
from app.db.vector_storage import VectorStorage
from .file_loader import FileLoaderRegistry

settings = Settings()
logger = initialize_logger(settings.log_level)

class FileProcessor:
    def process_files(self):
        process_status = []
        for root, _, files in os.walk(settings.files_path):
            for file in files:
                file_path = os.path.join(root, file)
                if self.process(file_path):
                    message = f"添加文档成功: {file_path}"
                else:
                    message = f"添加文档失败: {file_path}"
                logger.info(message)
                process_status.append(message)
        return process_status

    def process(self, file_path: str) -> Optional[str]:
        try:
            ext = os.path.splitext(file_path)[1].lower()
            loader_cls = FileLoaderRegistry.get_loader(ext)
            document_text = loader_cls().load(file_path)
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=settings.chunk_size,
                chunk_overlap=settings.chunk_overlap
            )
            split_texts = text_splitter.split_documents(document_text)
            vector_db = VectorStorage.create_storage("chroma")
            status = vector_db.store_documents(split_texts)
            return status
        except Exception as e:
            message = f"添加文档失败: {file_path}: {str(e)}"
            logger.error(message)
            return {"error": message}
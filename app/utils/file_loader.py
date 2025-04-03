from abc import ABC, abstractmethod
from typing import List, Type
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, UnstructuredExcelLoader
from app.config import Settings
from app.logger import initialize_logger

settings = Settings()
logger = initialize_logger(settings.log_level)

class FileLoader(ABC):
    @abstractmethod
    def load(self, file_path: str):
        pass

class FileLoaderRegistry:
    _registry = {}

    @classmethod
    def register(cls, extension: str):
        def decorator(loader_cls: Type[FileLoader]):
            cls._registry[extension] = loader_cls
            return loader_cls
        return decorator

    @classmethod
    def get_loader(cls, extension: str) -> Type[FileLoader]:
        if extension not in cls._registry:
            raise ValueError(f"不支持的文件类型: {extension}")
        return cls._registry[extension]

@FileLoaderRegistry.register(".pdf")
class PdfLoader(FileLoader):
    def load(self, file_path: str) -> List:
        try:
            document_text = PyPDFLoader(file_path).load()
            return document_text
        except Exception as e:
            logger.error(f"读取PDF文件发生错误 {file_path}: {e}")

@FileLoaderRegistry.register(".docx")
class DocxLoader(FileLoader):
    def load(self, file_path: str) -> List:
        try:
            document_text = Docx2txtLoader(file_path).load()
            return document_text
        except Exception as e:
            logger.error(f"读取Docx文件发生错误 {file_path}: {e}")

@FileLoaderRegistry.register(".xlsx")
class XlsxLoader(FileLoader):
    def load(self, file_path: str) -> List:
        try:
            document_text = UnstructuredExcelLoader(file_path).load()
            return document_text
        except Exception as e:
            logger.error(f"读取Xlsx文件发生错误 {file_path}: {e}")
import os
from enum import Enum
from dotenv import load_dotenv
from pathlib import Path
from pydantic import Field, RedisDsn
from pydantic_settings import BaseSettings

load_dotenv()
class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class Settings(BaseSettings):
    # 应用基础配置
    app_name: str = Field(env="APP_NAME")
    app_description: str = Field(env="APP_DESCRIPTION")
    app_version: str = Field(env="APP_VERSION")
    docs_url: str = Field(env="DOCS_URL")
    redoc_url: str = Field(env="REDOC_URL")
    environment: str = Field(env="ENVIRONMENT")
    debug: bool = Field(env="DEBUG")
    log_level: LogLevel = Field(env="LOG_LEVEL")
    
    # 模型配置
    model_name: str = Field(env="MODEL_NAME")
    temperature: float = Field(env="TEMPERATURE")
    max_tokens: int = Field(env="MAX_TOKENS")

    openai_api_key: str = Field(env="OPENAI_API_KEY")

    zhipuai_api_key: str = Field(env="ZHIPUAI_API_KEY")
    zhipuai_api_base: str = Field(env="ZHIPUAI_API_BASE")
    zhipuai_api_model: str = Field(env="ZHIPUAI_API_MODEL")
    zhipuai_api_embedding: str = Field(env="ZHIPUAI_API_EMBEDDING")

    deepseek_api_key: str = Field(env="DEEPSEEK_API_KEY")
    deepseek_api_base: str = Field(env="DEEPSEEK_API_BASE")
    deepseek_api_model: str = Field(env="DEEPSEEK_API_MODEL")

    # 数据库配置
    redis_url: RedisDsn = Field(env="REDIS_URL")
    cache_ttl: int = Field(env="CACHE_TTL")

    vector_db_host: str = Field(env="VECTOR_DB_HOST")
    vector_db_port: str = Field(env="VECTOR_DB_PORT")
    
    # 检索配置
    top_k_retrieval: int = Field(env="TOP_K_RETRIEVAL")
    chunk_size: int = Field(env="CHUNK_SIZE")
    chunk_overlap: int = Field(env="CHUNK_OVERLAP")
    
    # 向量存储配置
    files_path: Path = Field(env="FILES_PATH")
    vector_store_path: Path = Field(env="VECTOR_STORE_PATH")
    nexus_rag_collection: str = Field("nexus_rag_collection", env="VECTOR_COLLECTION_NAME")
    similarity_threshold: float = Field(0, ge=0.0, le=1.0, env="SIMILARITY_THRESHOLD")
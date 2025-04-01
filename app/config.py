from pydantic import BaseSettings, Field, RedisDsn, PostgresDsn, AnyUrl, validator
from typing import Optional, List, Dict, Any
from enum import Enum
import logging
from pathlib import Path

class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class EmbeddingModelType(str, Enum):
    OPENAI = "openai"
    HUGGINGFACE = "huggingface"
    COHERE = "cohere"
    LOCAL = "local"

class Settings(BaseSettings):
    # 应用基础配置
    app_name: str = Field("Enterprise RAG Agent", env="APP_NAME")
    app_version: str = Field("0.0.1", env="APP_VERSION")
    environment: str = Field("production", env="ENVIRONMENT")
    debug: bool = Field(False, env="DEBUG")
    log_level: LogLevel = Field(LogLevel.INFO, env="LOG_LEVEL")
    
    # API密钥配置
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    google_api_key: Optional[str] = Field(None, env="GOOGLE_API_KEY")
    cohere_api_key: Optional[str] = Field(None, env="COHERE_API_KEY")
    huggingfacehub_api_token: Optional[str] = Field(None, env="HF_API_TOKEN")
    
    # 模型配置
    llm_model: str = Field("gpt-3.5-turbo", env="LLM_MODEL")
    embedding_model: str = Field("text-embedding-3-small", env="EMBEDDING_MODEL")
    embedding_model_type: EmbeddingModelType = Field(EmbeddingModelType.OPENAI, env="EMBEDDING_MODEL_TYPE")
    temperature: float = Field(0.7, ge=0.0, le=1.0, env="TEMPERATURE")
    max_tokens: int = Field(1024, gt=0, env="MAX_TOKENS")
    
    # 数据库配置
    redis_url: RedisDsn = Field("redis://localhost:6379/0", env="REDIS_URL")
    cache_ttl: int = Field(3600, gt=0, env="CACHE_TTL")
    
    # 检索配置
    top_k_retrieval: int = Field(5, gt=0, env="TOP_K_RETRIEVAL")
    chunk_size: int = Field(1000, gt=0, env="CHUNK_SIZE")
    chunk_overlap: int = Field(200, ge=0, env="CHUNK_OVERLAP")
    
    # 向量存储配置
    vector_store_path: Path = Field(Path("./data/vector_store"), env="VECTOR_STORE_PATH")
    similarity_threshold: float = Field(0.75, ge=0.0, le=1.0, env="SIMILARITY_THRESHOLD")
    
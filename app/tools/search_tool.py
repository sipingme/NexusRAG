from langchain.tools import tool
from app.cache.redis_manager import cache_result

@tool
@cache_result(ttl=3600)
def web_search(query: str) -> str:
    """执行网页搜索并返回结果"""
    # 实际搜索实现
    return f"Results for {query}"
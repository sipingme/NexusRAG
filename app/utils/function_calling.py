from typing import List, Dict, Any
from langchain_core.messages import AIMessage, HumanMessage

def process_function_calling(messages: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """处理函数调用消息"""
    processed = []
    for msg in messages:
        if msg.get("function_call"):
            processed.append(AIMessage(
                content=msg.get("content", ""),
                additional_kwargs={"function_call": msg["function_call"]}
            ))
        else:
            processed.append(HumanMessage(content=msg["content"]))
    return processed
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.models.mcp import MCPRequest, MCPResponse
from app.agents.rag_agent import RAGAgent
from app.tools.search_tool import web_search
import logging

app = FastAPI(title="Enterprise RAG Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agent with tools
tools = [web_search]
agent = RAGAgent(tools)

@app.post("/v1/chat/completions", response_model=MCPResponse)
async def chat_completion(request: MCPRequest):
    try:
        if not request.messages:
            raise HTTPException(status_code=400, detail="No messages provided")
        
        last_message = request.messages[-1]
        if last_message.role != "user":
            raise HTTPException(status_code=400, detail="Last message must be from user")
        
        return await agent.run(last_message.content, request.messages[:-1])
    
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
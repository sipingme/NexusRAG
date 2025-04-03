import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.config import Settings
from app.logger import initialize_logger
from app.utils.file_processor import FileProcessor
from app.chains.qa_chain import QAChain

settings = Settings()
logger = initialize_logger(settings.log_level)

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# tools = [web_search]
# agent = RAGAgent(tools)

@app.get("/")
def root():
    return {"message": settings.app_description}

@app.get("/chat")
async def chat(request: Request):
    try:
        query = request.query_params.get("query", "")
        chain = QAChain()
        result = chain.executor(query)
        return result
    except Exception as e:
        message = f"请求处理失败: {e}"
        logger.error(message)
        return {"error": message}

@app.get("/add_files")
async def add_files():
    try:
        processor = FileProcessor()
        status = processor.process_files()
        return status
    except Exception as e:
        message = f"添加文档失败: {e}"
        logger.error(message)
        return {"error": message}
    
@app.get("/query_file")
def query_file(request: Request):
    query = request.query_params.get("query", "")
    logger.info(f"查询文档接口被访问: {query}")

@app.get("/delete_file")
def delete_file(request: Request):
    query = request.query_params.get("query", "")
    logger.info(f"删除文档接口被访问: {query}")

# @app.post("/v1/chat/completions", response_model=MCPResponse)
# async def chat_completion(request: MCPRequest):
#     try:
#         if not request.messages:
#             raise HTTPException(status_code=400, detail="No messages provided")
        
#         last_message = request.messages[-1]
#         if last_message.role != "user":
#             raise HTTPException(status_code=400, detail="Last message must be from user")
        
#         return await agent.run(last_message.content, request.messages[:-1])
    
#     except Exception as e:
#         logging.error(f"Error processing request: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    logger.info("启动服务器")
    uvicorn.run(
        app="app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["app"],
        log_level="debug",
        workers=1
    )
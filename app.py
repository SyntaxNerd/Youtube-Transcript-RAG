from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from main import rag_pipeline, ask_question, video_rag_system, video_chat_history

# initialize fastapi
app = FastAPI()

# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# base model class
class RagRequest(BaseModel):
    video_id: Optional[str] = None
    query: Optional[str] = None

# endpoint
@app.post("/home")
async def rag_endpoint(request: RagRequest):
    response = {}

    if request.video_id:
        if request.video_id not in video_rag_system:
            try:
                response["message"] = rag_pipeline(request.video_id)
            except Exception as e:
                raise HTTPException(status_code = 500, detail = f"Failed to build the pipeline: {str(e)}")
        
        else:
            response["message"] = f"Pipeline already exists for video {request.video_id}"

    if request.query:
        if not request.video_id:
            raise HTTPException(status_code = 500, detail = "Video ID is required to ask a question")
        try:
            response["query"] = request.query
            response["answer"] = ask_question(request.video_id, request.query)
        except Exception as e:
            raise HTTPException(status_code = 500, detail = f"Failed to get the answer: {str(e)}")
        
    if not response:
        raise HTTPException(status_code = 400, detail = "Please provide a video_id or query")

    return response
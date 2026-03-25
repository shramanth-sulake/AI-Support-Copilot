from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.postgres import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent import chat_with_agent

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    result = chat_with_agent(
        request.message,
        db,
        request.session_id
    )
    return result
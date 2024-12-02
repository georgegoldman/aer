from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ChatHistory
from app.schemas import ChatRequest, ChatResponse
from app.services import get_chatgpt_response

router  = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/send-message", response_model=ChatResponse)
async def send_message(chat: ChatRequest, db: Session = Depends(get_db)):
    response_text = get_chatgpt_response(chat.context, chat.message)

    # Save chat history
    chat_history = ChatHistory(
        user_id=chat.user_id,
        context=chat.context,
        message=chat.message,
        response=response_text
    )

    db.add(chat_history)
    db.commit()

    return {"response": response_text}
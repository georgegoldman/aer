from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    user_id: str
    context: Optional[str] = None
    message: str

class ChatResponse(BaseModel):
    response: str
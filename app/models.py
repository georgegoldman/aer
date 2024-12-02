from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base # type: ignore
from datetime import datetime

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    context = Column(Text)
    message = Column(Text)
    response = Column(Text)
    create_at = Column(DateTime, default=datetime.now())

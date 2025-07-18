# SQLAlchemy modelleri
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base
from uuid import uuid4
from datetime import datetime

Base = declarative_base()

class Conversation(Base):
    #"""
    #sessions
    #user_token: Cookie veya session ile gelen usera özel token
    #"""
    __tablename__ = "conversations"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    user_token = Column(String, nullable=False)  # tarayıcıya atanacak eşsiz token
    created_at = Column(DateTime, default=datetime.utcnow)

    # 1 konuşma - > n mesaj
    messages = relationship("Message", back_populates="conversation", cascade="all, delete-orphan")


class Message(Base):
    #user ve asistan tekil messages
    __tablename__ = "messages"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    conversation_id = Column(String, ForeignKey("conversations.id"), nullable=False)

    role = Column(String, nullable=False)          # user | assistant | system
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # hangi mesaj hangi session 
    conversation = relationship("Conversation", back_populates="messages")

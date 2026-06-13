from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from datetime import datetime

from database import Base


class FAQ(Base):
    __tablename__ = "faqs"

    id = Column(Integer, primary_key=True, index=True)

    category = Column(String(100), nullable=False)

    question = Column(Text, nullable=False)

    answer = Column(Text, nullable=False)


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    user_question = Column(Text, nullable=False)

    matched_question = Column(Text, nullable=False)

    bot_answer = Column(Text, nullable=False)

    confidence = Column(Float, nullable=False)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )
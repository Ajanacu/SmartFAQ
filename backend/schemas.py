from pydantic import BaseModel
from typing import List


# -----------------------------
# Request Models
# -----------------------------

class ChatRequest(BaseModel):
    question: str


class NewChatRequest(BaseModel):
    title: str = "New Chat"


# -----------------------------
# Response Models
# -----------------------------

class ChatResponse(BaseModel):
    answer: str
    confidence: float
    matched_question: str
    related_questions: List[str]


class FAQResponse(BaseModel):
    id: int
    category: str
    question: str
    answer: str

    class Config:
        from_attributes = True


class HistoryItem(BaseModel):
    id: int
    user_question: str
    matched_question: str
    bot_answer: str
    confidence: float
    timestamp: str

    class Config:
        from_attributes = True
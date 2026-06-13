from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import datetime

from database import engine, Base, get_db
from models import FAQ, ChatHistory
from faq_matcher import FAQMatcher
from schemas import ChatRequest

app = FastAPI(title="SmartFAQ AI Assistant")

# -----------------------
# Enable CORS
# -----------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Later replace with React URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Create Database Tables
# -----------------------

Base.metadata.create_all(bind=engine)

# -----------------------
# Load Semantic Matcher
# -----------------------

matcher = FAQMatcher()


# -----------------------
# Home
# -----------------------

@app.get("/")
def home():
    return {
        "message": "SmartFAQ AI Assistant Backend Running"
    }


# -----------------------
# Get FAQs
# -----------------------

@app.get("/faqs")
def get_faqs():

    return matcher.faqs


# -----------------------
# Chat Endpoint
# -----------------------

@app.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    result = matcher.find_best_match(
        request.question
    )

    history = ChatHistory(
        user_question=request.question,
        matched_question=result["matched_question"],
        bot_answer=result["answer"],
        confidence=result["confidence"]
    )

    db.add(history)
    db.commit()

    return result


# -----------------------
# Get History
# -----------------------

@app.get("/history")
def history(
    db: Session = Depends(get_db)
):

    chats = (
        db.query(ChatHistory)
        .order_by(ChatHistory.id.desc())
        .all()
    )

    output = []

    for chat in chats:

        output.append(
            {
                "id": chat.id,
                "user_question": chat.user_question,
                "matched_question": chat.matched_question,
                "bot_answer": chat.bot_answer,
                "confidence": chat.confidence,
                "timestamp": chat.timestamp
            }
        )

    return output


# -----------------------
# Save History
# -----------------------

@app.post("/history")
def save_history(
    request: ChatRequest,
    db: Session = Depends(get_db)
):

    result = matcher.find_best_match(
        request.question
    )

    history = ChatHistory(
        user_question=request.question,
        matched_question=result["matched_question"],
        bot_answer=result["answer"],
        confidence=result["confidence"]
    )

    db.add(history)
    db.commit()

    return {
        "message": "Saved"
    }


# -----------------------
# New Chat
# -----------------------

@app.post("/new-chat")
def new_chat():

    return {
        "message": "New chat created"
    }
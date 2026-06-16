# SmartFAQ AI Assistant

An AI-powered FAQ chatbot built using **React**, **FastAPI**, and **Natural Language Processing (NLP)** to provide intelligent responses through semantic similarity instead of exact keyword matching.

## Live Demo

 https://smart-faq-theta.vercel.app/
 
---

# Overview

SmartFAQ AI Assistant is a full-stack web application that enables users to ask questions in natural language and receive the most relevant answer from a knowledge base. The system uses NLP-based similarity techniques to understand user intent, calculate confidence scores, and recommend related questions.

The application features a modern chat interface inspired by contemporary AI assistants and demonstrates frontend-backend integration using REST APIs.

---

# Features

* Semantic FAQ matching using NLP techniques
* Confidence score for each response
* Related question recommendations
* Modern chat interface
* Typing indicator animation
* New Chat functionality
* Dark and Light mode support
* FastAPI backend with REST architecture

---

# Tech Stack

## Frontend

* React
* Axios
* CSS

## Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite

## Machine Learning

* Sentence Transformers (all-MiniLM-L6-v2)
* Scikit-learn
* Cosine Similarity
* Semantic Search

---

# Project Structure

```text
SmartFAQ-AI/

├── backend/
│   ├── app.py
│   ├── database.py
│   ├── faq_matcher.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   └── data/
│       └── faqs.json
│
├── frontend/
│   ├── public/
│   └── src/
│       ├── components/
│       ├── App.js
│       └── App.css
│
└── README.md
```

---

# How It Works

1. The user submits a question through the chat interface.
2. The backend preprocesses the query.
3. NLP-based similarity is computed against the FAQ dataset.
4. The most relevant FAQ is selected.
5. The application returns:

   * Answer
   * Confidence score
   * Related questions

---

# Screenshots

<img width="1912" height="927" alt="Screenshot 2026-06-13 195538" src="https://github.com/user-attachments/assets/d5a14f4d-e025-465d-91aa-9589dde02cd0" />

<img width="1918" height="921" alt="Screenshot 2026-06-13 195623" src="https://github.com/user-attachments/assets/0ad86f25-2742-4d86-a189-76c0a5db4f1c" />

---

# Installation

## Clone the repository

```bash
git clone https://github.com/Ajanacu/SmartFAQ.git
cd SmartFAQ
```

## Backend Setup

```bash
cd backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
uvicorn app:app --reload
```

## Frontend Setup

```bash
cd frontend

npm install
npm start
```

The application will be available at:

* Frontend: `http://localhost:3000`
* Backend: `http://127.0.0.1:8000`

---

# Future Improvements

* Multi-language support
* User authentication
* Voice-based interactions
* Admin dashboard for FAQ management
* Analytics and usage insights
* Vector database integration
* LLM-powered fallback responses

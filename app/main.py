# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# chatt endpoints
from app.chat.api import router as chat_router

app = FastAPI(title="🎬 Movie Chatbot API")

# CORS ->  frontend Streamlit 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# chat router
app.include_router(chat_router)

print("chat module loaded")

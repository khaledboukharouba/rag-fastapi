from fastapi import FastAPI
from app.api import api_router

app = FastAPI(title="RAG FastAPI with Gemini")

app.include_router(api_router.router)
from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="AI PDF Q&A System",
    description="A RAG-based application for asking questions from PDF documents.",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI PDF Q&A System"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
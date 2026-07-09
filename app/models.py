from pydantic import BaseModel
from typing import List


class UploadResponse(BaseModel):
    filename: str
    message: str
    total_chunks: int


class QuestionRequest(BaseModel):
    question: str


class QuestionResponse(BaseModel):
    question: str
    answer: str
    context: List[str]
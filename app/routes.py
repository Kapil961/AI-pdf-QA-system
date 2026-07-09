import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.models import UploadResponse, QuestionRequest, QuestionResponse
from app.pdf_handler import PDFHandler
from app.chunker import Chunker
from app.embedding import EmbeddingModel
from app.vector_store import VectorStore
from app.retriever import Retriever
from app.prompt_builder import PromptBuilder
from app.llm import LLM


router = APIRouter()

UPLOAD_DIR = "uploads"

vector_store = VectorStore()
prompt_builder = PromptBuilder()
llm = LLM()


@router.post("/upload-pdf", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pdf_handler = PDFHandler()
    text = pdf_handler.extract_text(file_path)

    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="No text found inside the uploaded PDF."
        )

    chunker = Chunker()
    chunks = chunker.create_chunks(text)

    embedding_model = EmbeddingModel()
    embeddings = embedding_model.generate_embeddings(chunks)

    vector_store.store_embeddings(chunks, embeddings)

    return UploadResponse(
        filename=file.filename,
        message="PDF processed successfully.",
        total_chunks=len(chunks)
    )


@router.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    if vector_store.count_documents() == 0:
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF first."
        )

    retriever = Retriever()

    results = retriever.retrieve(
        question=request.question,
        top_k=3
    )

    retrieved_chunks = results["documents"][0]

    prompt = prompt_builder.build_prompt(
        question=request.question,
        retrieved_chunks=retrieved_chunks
    )

    answer = llm.generate_answer(prompt)

    return QuestionResponse(
        question=request.question,
        answer=answer,
        context=retrieved_chunks
    )
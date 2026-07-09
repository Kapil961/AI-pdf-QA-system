# 📄 AI PDF Q&A System (RAG)

A Retrieval-Augmented Generation (RAG) application built using **FastAPI**, **Sentence Transformers**, **ChromaDB**, and **Gradio**.

The application allows users to upload PDF documents and ask questions based on their content using semantic search.

---

## 🚀 Features

- Upload PDF documents
- Extract text from PDF
- Split text into chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in ChromaDB
- Semantic similarity search
- Prompt generation
- FastAPI backend
- Gradio frontend
- Modular project structure

---

## 🛠️ Tech Stack

- Python 3.11
- FastAPI
- Gradio
- Sentence Transformers
- ChromaDB
- PyPDF
- OpenAI SDK (LLM Ready)
- NumPy

---

## 📂 Project Structure

```
ai-pdf-qa-system/
│
├── app/
│   ├── models.py
│   ├── pdf_handler.py
│   ├── chunker.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompt_builder.py
│   ├── llm.py
│   └── routes.py
│
├── frontend/
│   └── gradio_app.py
│
├── uploads/
├── chroma_db/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
cd ai-pdf-qa-system
```

Create a virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Backend

```bash
python -m uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend

```bash
python frontend/gradio_app.py
```

Frontend URL

```
http://127.0.0.1:7860
```

---

## 🔄 RAG Pipeline

```
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Create Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Build Prompt
      │
      ▼
LLM
      │
      ▼
Answer
```

---

## 📌 Current Status

- ✅ FastAPI Backend
- ✅ PDF Processing
- ✅ Chunking
- ✅ Embeddings
- ✅ ChromaDB
- ✅ Semantic Retrieval
- ✅ Prompt Builder
- ✅ Gradio Frontend
- ⏳ Replace Mock LLM with a production LLM (OpenAI/Groq/Gemini)

---

## 👨‍💻 Author

**Kapil Kumawat**

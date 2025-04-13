from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from app.services.pdf_loader import load_pdf_text
from app.services.rag_service import ingest_text_to_vectorstore, answer_question

router = APIRouter()


# Health check
@router.get("/health")
async def health():
    return {"status": "ok"}


# Upload a PDF and add to Chroma vector store
@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    text = load_pdf_text(file)
    ingest_text_to_vectorstore(text)
    return {"status": "uploaded and indexed"}


# Query the vector DB + Gemini
class QueryRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask_question(request: QueryRequest):
    answer = await answer_question(request.question)  # make async call to answer_question
    return {"answer": answer}

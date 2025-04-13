from langchain.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from app.core.config import settings

embedding = GoogleGenerativeAIEmbeddings(google_api_key=settings.GOOGLE_API_KEY, model="models/text-embedding-004")

def get_vectorstore():
    return Chroma(collection_name="rag_collection", embedding_function=embedding, persist_directory=settings.CHROMA_DB_DIR)

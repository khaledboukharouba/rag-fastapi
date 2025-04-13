from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI
from app.core.config import settings
from app.core.vectorstore import get_vectorstore
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

def ingest_text_to_vectorstore(text: str):
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents([Document(page_content=text)])
    vectordb = get_vectorstore()
    vectordb.add_documents(docs)
    vectordb.persist()

# Make answer_question async
async def answer_question(query: str) -> str:
    vectordb = get_vectorstore()
    retriever = vectordb.as_retriever()
    llm = GoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=settings.GOOGLE_API_KEY)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
    return await qa_chain.arun(query)  # Use async method for running queries

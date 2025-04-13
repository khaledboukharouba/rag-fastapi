# RAG FastAPI App

A production-ready **Retrieval-Augmented Generation (RAG)** API using:

- **FastAPI** – lightning-fast web framework  
- **Google Gemini API** – LLM for answering questions  
- **ChromaDB** – lightweight vector store  
- **LangChain** – integrates LLMs with vector store  
- **Docker & Compose** – containerized, reproducible dev environment  
- PDF ingestion & embedding with LangChain

---

## Features

- `/health` – Health check
- `/upload-pdf` – Upload a PDF file and index its content
- `/ask` – Ask questions based on embedded documents (RAG)
- Asynchronous 
- Ready for deployment with Docker
- Unit tested with `pytest`

---

## Project Structure
rag_fastapi/
├── app/
│   ├── api/               # Endpoints 
│   ├── core/              # Configs and vector store setup
│   ├── services/          # PDF ingestion & RAG logic
│   └── main.py            
├── tests/                 # Unit tests
├── Dockerfile
├── docker-compose.yml
├── .env                   # Environment variables 
├── .gitignore
└── README.md


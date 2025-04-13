import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_upload_pdf():
    with open("tests/sample.pdf", "rb") as f:
        response = client.post("/upload-pdf", files={"file": ("sample.pdf", f, "application/pdf")})
    assert response.status_code == 200
    assert response.json()["status"] == "uploaded and indexed"

def test_ask():
    payload = {"question": "What is this document about?"}
    response = client.post("/ask", json=payload)
    assert response.status_code == 200
    assert "answer" in response.json()

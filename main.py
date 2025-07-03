from fastapi import FastAPI
from pydantic import BaseModel
from rag_core import get_answer  # must be working

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/query")
def query_endpoint(q: Query):
    try:
        answer = get_answer(q.question)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"message": "RAG API is running"}

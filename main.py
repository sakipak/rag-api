from fastapi import FastAPI
from pydantic import BaseModel
from rag_core import ask_question

app = FastAPI()

class Query(BaseModel):
    question: str

    
@app.post("/query")
def query(q: Query):
    answer = ask_question(q.question)
    return {"answer": answer}    

@app.get("/")
def home():
    return {"message": "RAG API is running"}

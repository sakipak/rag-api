from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_core import get_answer

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/query")
def query_endpoint(q: Query):
    try:
        answer = get_answer(q.question)
        return {"answer": answer}
    except Exception as e:
        # Return error details to help debug
        raise HTTPException(status_code=500, detail=str(e))

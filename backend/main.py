from fastapi import FastAPI, Query
from rag_engine import retrieve_docs
from vertex_ai_llm import query_llm

app = FastAPI()

@app.get("/ask")
def ask(question: str = Query(...)):
    context = retrieve_docs(question)
    response = query_llm(question, context)
    return {"text": response}
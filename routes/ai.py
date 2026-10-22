from fastapi import APIRouter, HTTPException
from ai_engine.rag_pipeline import ask
from models.ask import AskRequest

router = APIRouter()

@router.post("/ai/ask")
def ask_ai_endpoint(request: AskRequest):
    try:
        result = ask(request.query)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

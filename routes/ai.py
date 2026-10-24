from fastapi import APIRouter, HTTPException, Request
from ai_engine.rag_pipeline import ask
from models.ask import AskRequest
from limiter import limiter

router = APIRouter()

@router.post("/ai/ask")
@limiter.limit("10/minute")
def ask_ai_endpoint(request: Request, body: AskRequest):
    try:
        result = ask(body.query)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
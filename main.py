from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from limiter import limiter
from routes.restaurants import router as restaurant_router
from routes.auth import router as auth_router
from routes.students import router as student_router
from routes.orders import router as order_router
from routes.recommendation import router as recommendation_router
from routes.ai import router as ai_router
import logging
import time


app = FastAPI()


logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    logger.info(f"{request.method} {request.url.path} {response.status_code} {duration:.2f}s")
    return response

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error on {request.method} {request.url}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(restaurant_router)
app.include_router(auth_router)
app.include_router(student_router)
app.include_router(order_router)
app.include_router(recommendation_router)
app.include_router(ai_router)
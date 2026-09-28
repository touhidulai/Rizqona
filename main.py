from fastapi import FastAPI
from routes.restaurants import router as restaurant_router
from routes.auth import router as auth_router

app = FastAPI()

app.include_router(restaurant_router)
app.include_router(auth_router)

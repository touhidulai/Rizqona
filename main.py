from fastapi import FastAPI
from routes.restaurants import router

app = FastAPI()

app.include_router(router)


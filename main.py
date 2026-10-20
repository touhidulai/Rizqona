from fastapi import FastAPI
from routes.restaurants import router as restaurant_router
from routes.auth import router as auth_router
from routes.students import router as student_router
from routes.orders import router as order_router
from routes.recommendation import router as recommendation_router

app = FastAPI()

app.include_router(restaurant_router)
app.include_router(auth_router)
app.include_router(student_router)
app.include_router(order_router)
app.include_router(recommendation_router)

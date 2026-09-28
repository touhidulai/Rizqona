from fastapi import APIRouter, HTTPException
from models.users import UserCreate, UserResponse, UserLogin
from services.auth_service import hash_password, verify_password, create_token, verify_token
from database.repository import create_user,get_user_by_username

router = APIRouter()

@router.post("/register")
def register_user_endpoint(user: UserCreate):

    raw_password = user.password
    hashed_password = hash_password(raw_password)

    try:
        return create_user(user.name, user.username, user.email, user.phone_number, hashed_password)
    except Exception as e:
        raise HTTPException(status_code = 400, detail = {str(e)})

@router.post ("/auth/login")
def login_endpoint(login_user: UserLogin):

    user = get_user_by_username(login_user.username)

    if user is None:
        raise HTTPException(status_code = 404, detail = "User not found")

    if verify_password(login_user.password, user["password"]):
        return create_token(user["id"])
    else:
        raise HTTPException(status_code = 401, detail="Wrong Credentials")
import jwt
import os
import bcrypt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_token(token)
        return payload["user_id"]
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


def hash_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(raw_password: str, hashed_password: str):
    return bcrypt.checkpw(raw_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_token(user_id: int):
    SECRET_KEY = os.getenv("SECRET_KEY")
    algorithm = "HS256"

    return jwt.encode({"user_id": user_id}, SECRET_KEY, algorithm=algorithm)

def verify_token(token: str):
    SECRET_KEY = os.getenv("SECRET_KEY")
    algorithm = "HS256"
    return jwt.decode(token, SECRET_KEY, algorithms=[algorithm])
import jwt
import os
import bcrypt


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
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    phone_number: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    phone_number: str
    
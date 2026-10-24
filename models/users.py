from pydantic import BaseModel, EmailStr, Field, field_validator


class UserCreate(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    phone_number: str = Field(min_length=10, max_length=12)
    password: str = Field(min_length=8)

    @field_validator('password')
    @classmethod
    def validate_password(cls, value):
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least 1 digit")
        return value

class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    phone_number: str

class UserLogin(BaseModel):
    username: str
    password: str
    
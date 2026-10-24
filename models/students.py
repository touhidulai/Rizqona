from pydantic import BaseModel, EmailStr, field_validator, Field


class StudentCreate(BaseModel):

    name: str = Field(min_length = 3, max_length = 30)
    username: str = Field(min_length = 3, max_length = 30)
    email: EmailStr
    phone_number: str = Field(min_length = 10, max_length = 12)
    password: str = Field(min_length = 8)

    @field_validator('email')
    def email_must_be_um(cls, v):
        if not v.endswith('@siswa.um.edu.my'):
            raise ValueError("Must use a UM student email")
        return v

    @field_validator('password')
    def validate_password(cls, value):
        if not any(char.isdigit() for char in value):
            raise ValueError("Password needs at least 1 digits")
        return value

class StudentResponse(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    phone_number: str

class StudentLogin(BaseModel):
    email: str
    password: str


from pydantic import BaseModel, EmailStr, field_validator


class StudentCreate(BaseModel):

    name: str
    username: str
    email: EmailStr
    phone_number: str
    password: str

    @field_validator('email')
    def email_must_be_um(cls, v):
        if not v.endswith('@siswa.um.edu.my'):
            raise ValueError("Must use a UM student email")
        return v

class StudentResponse(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    phone_number: str

class StudentLogin(BaseModel):
    email: str
    password: str


from fastapi import APIRouter, HTTPException, Depends
from database.student_repository import create_student, get_student_by_email, get_student_by_id 
from models.students import StudentCreate,StudentResponse, StudentLogin 
from services.auth_service import get_current_user, hash_password, verify_password, create_token


router = APIRouter()

@router.post("/student-register")
def register_student_endpoint(student: StudentCreate):

    raw_password = student.password
    hashed_password = hash_password(raw_password)

    try:
        return create_student(student.name, student.username, student.email, student.phone_number, hashed_password)
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))

@router.post ("/auth/student-login")
def student_login_endpoint(login_student: StudentLogin):

    user = get_student_by_email(login_student.email)

    if user is None:
        raise HTTPException(status_code = 404, detail = "User not found")

    if verify_password(login_student.password, user["password"]):
        return create_token(user["id"])
    else:
        raise HTTPException(status_code = 401, detail="Wrong Credentials")

@router.get("/students/me")
def get_student_info( current_user: int = Depends(get_current_user)):

    user = get_student_by_id(current_user)
    if user is None:
        raise HTTPException(status_code = 404, detail = "Student Not Found")
    return user

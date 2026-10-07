from database.connection import get_connection
from psycopg2.extras import RealDictCursor

def create_student(name, username, email, phone_number, password, role = "student"):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("INSERT INTO users (name, username,email,phone_number, password, role) VALUES (%s,%s,%s,%s,%s, %s) RETURNING id", (name,username, email, phone_number,password,role,))
        user_id = cursor.fetchone()["id"]
        cursor.execute("INSERT INTO student_profiles (user_id) VALUES (%s)", (user_id,))
        conn.commit()
        return {"message": f"Student with {username} is registered. Student id is: {user_id}"}
    except Exception as e:
        conn.rollback()
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def get_student_by_email(email: str):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("SELECT * FROM users WHERE email = (%s)",(email,))
        user = cursor.fetchone()
        return user
    except Exception as e:
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def get_student_by_id(id: int):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("SELECT id, name, username, email, phone_number FROM users WHERE id = (%s)",(id,))
        user = cursor.fetchone()
        return user
    except Exception as e:
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()
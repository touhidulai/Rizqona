# from database.connection import get_connection
# from psycopg2.extras import RealDictCursor

# def create_user(name, username, email, phone_number, password):
#     conn = get_connection()
#     cursor = conn.cursor(cursor_factory = RealDictCursor)

#     try:
#         cursor.execute("INSERT INTO users (name, username,email,phone_number, password) VALUES (%s,%s,%s,%s,%s) RETURNING id", (name,username, email, phone_number,password, ))
#         user_id = cursor.fetchone()["id"]
#         conn.commit()
#         return {"message": f"Users with {username} is registered. User id is: {user_id}"}
#     except Exception as e:
#         conn.rollback()
#         raise ValueError(f"Something went wrong: {str(e)}")
#     finally:
#         cursor.close()
#         conn.close()


# def get_user_by_username(username: str):
#     conn = get_connection()
#     cursor = conn.cursor(cursor_factory = RealDictCursor)

#     try:
#         cursor.execute("SELECT * FROM users WHERE username = (%s)",(username,))
#         user = cursor.fetchone()
#         return user
#     except Exception as e:
#         raise ValueError(f"Something went wrong: {str(e)}")
#     finally:
#         cursor.close()
#         conn.close()
from database.connection import get_connection
from psycopg2.extras import RealDictCursor

def create_event(student_id, event_type, restaurant_id=None, menu_item_id = None):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)
    
    try:
        cursor.execute("INSERT INTO events (student_id, event_type, restaurant_id, menu_item_id) VALUES (%s, %s, %s, %s) RETURNING id", (student_id, event_type, restaurant_id,menu_item_id,))
        log_id = cursor.fetchone()["id"]
        conn.commit()
        return {"log_id": f"Log {log_id} is succesful"}
    except Exception as e:
        conn.rollback()
        raise ValueError(f"Failed to add log: {str(e)}")
    finally:
        cursor.close()
        conn.close()
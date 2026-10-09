from database.connection import get_connection
from psycopg2.extras import RealDictCursor

def add_to_cart(student_id, menu_item_id, quantity):

    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)
    
    try:
        cursor.execute("INSERT INTO cart_items (student_id, menu_item_id, quantity) VALUES (%s, %s, %s) RETURNING id", (student_id, menu_item_id, quantity,))
        cart_item_id = cursor.fetchone()["id"]
        conn.commit()
        return {"Cart Item ID": cart_item_id}
    except Exception as e:
        conn.rollback()
        raise ValueError(f"Failed to add item to the cart: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def get_cart(student_id):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)
    
    try:
        cursor.execute("SELECT cart_items.*, menu_items.price, menu_items.restaurant_id FROM cart_items JOIN menu_items ON cart_items.menu_item_id = menu_items.id WHERE cart_items.student_id = %s", (student_id,))
        cart_item = cursor.fetchall()
        return {"Cart Item": cart_item}
    except Exception as e:
        raise ValueError(f"Failed to retrieve cart item: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def place_order(student_id):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)
    
    try:
        total_price = 0
        cart_item = get_cart(student_id)
        if len(cart_item["Cart Item"]) == 0:
            return {"Message": "Empty cart can't be ordered"}
        for item in cart_item["Cart Item"]:
            total_price += item["price"]

        cursor.execute("INSERT INTO orders (student_id, restaurant_id, total_price, status) VALUES (%s, %s, %s, %s) RETURNING id", (student_id, cart_item["Cart Item"][0]["restaurant_id"], total_price, "pending",))
        order_id = cursor.fetchone()["id"]
        for item in cart_item["Cart Item"]:
            cursor.execute("INSERT INTO order_items (order_id, menu_item_id, quantity, price) VALUES (%s, %s, %s, %s)", (order_id, item["menu_item_id"], item["quantity"], item["price"],))
            cursor.execute("DELETE FROM cart_items where id = %s",(item["id"],))
        conn.commit()
        return {"Message": "Congratulations! Order Confirmed"}
    except Exception as e:
        conn.rollback()
        raise ValueError(f"Failed to confirm Order. Something went Wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def get_orders(student_id):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)
    
    try:
        cursor.execute("SELECT * FROM orders WHERE student_id = %s", (student_id,))
        all_orders = cursor.fetchall()
        return {"Order Items": all_orders}
    except Exception as e:
        raise ValueError(f"Failed to retrieve orders: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def get_restaurant_orders(restaurant_id):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)
    
    try:
        cursor.execute("SELECT * FROM orders WHERE restaurant_id = %s", (restaurant_id,))
        all_orders = cursor.fetchall()
        return {"Order Items": all_orders}
    except Exception as e:
        raise ValueError(f"Failed to retrieve orders: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def update_order_status(order_id, status):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)
    
    try:
        cursor.execute("UPDATE orders SET status = %s WHERE id = %s", (status,order_id))
        conn.commit()
        return {"message": f"Order {order_id} status is updated to {status}"}
    except Exception as e:
        conn.rollback()
        raise ValueError(f"Failed to update order status: {str(e)}")
    finally:
        cursor.close()
        conn.close()
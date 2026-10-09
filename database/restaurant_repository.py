from database.connection import get_connection
from psycopg2.extras import RealDictCursor

def create_restaurant(name, phone_number, address, trade_license_no, photo_url, cuisine_type, opening_time, owner_id):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)
    
    try:
        cursor.execute("INSERT INTO restaurant (name, phone_number, address, trade_license_no, photo_url, cuisine_type, opening_time, owner_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id", (name, phone_number, address, trade_license_no, photo_url, cuisine_type, opening_time,owner_id))
        restaurant_id = cursor.fetchone()["id"]
        conn.commit()
        return {"restaurant_id": restaurant_id}
    except Exception as e:
        conn.rollback()
        raise ValueError(f"Failed to create restaurant: {str(e)}")
    finally:

        cursor.close()
        conn.close()
        
def get_all_restaurants():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("SELECT restaurant.name, restaurant.address, restaurant.photo_url, restaurant.cuisine_type, restaurant.opening_time FROM restaurant")
        restaurants = cursor.fetchall()
        return restaurants
    except Exception as e:
        raise ValueError(f"Something Wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def get_restaurant_by_id(id: int):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("SELECT restaurant.name, restaurant.address, restaurant.photo_url, restaurant.cuisine_type, restaurant.opening_time FROM restaurant WHERE id =(%s)", (id,))
        restaurant = cursor.fetchone()
        return restaurant
    except Exception as e:
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def create_menu_item(restaurant_id, name, price, portion_size, category, photo_url, is_available):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("INSERT INTO menu_items (restaurant_id, name, price, portion_size, category, photo_url, is_available) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id", (restaurant_id, name, price, portion_size, category, photo_url, is_available,))
        item_id = cursor.fetchone()["id"]
        conn.commit()
        return {"menu_id": item_id}
    except Exception as e:
        conn.rollback()
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def update_menu_item_availability(id, is_available: bool):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("UPDATE menu_items SET is_available = (%s) WHERE id = (%s)", (is_available,id,))
        conn.commit()
        return {"message": f"Menu Items updated to {is_available}"}
    except Exception as e:
        conn.rollback()
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def get_full_menu_by_restaurant_id(restaurant_id):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("SELECT * FROM menu_items WHERE restaurant_id =(%s)", (restaurant_id,))
        menu = cursor.fetchall()
        return menu
    except Exception as e:
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def search_menu_items_by_name(name):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("SELECT * FROM menu_items WHERE name ILIKE %s", (f'%{name}%',))
        menus = cursor.fetchall()
        return menus
    except Exception as e:
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def filter_menu_items_by_price(max_price):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("SELECT * FROM menu_items WHERE price <= %s", (max_price,))
        menus = cursor.fetchall()
        return menus
    except Exception as e:
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def get_restaurant_by_owner_id(owner_id):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory = RealDictCursor)

    try:
        cursor.execute("SELECT id FROM restaurant WHERE owner_id =%s", (owner_id,))
        restaurant_id = cursor.fetchone()["id"]
        return restaurant_id
    except Exception as e:
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()
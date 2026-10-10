import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import get_connection
from services.auth_service import hash_password
import random
from datetime import datetime, timedelta
from scripts.seed_data import owners, restaurants, menu_items, faculties, students

# def seed_owners(name,username, email, phone_number, password, role= "owner"):
#     conn = get_connection()
#     cursor = conn.cursor()

#     try:
#         cursor.execute("INSERT INTO users (name, username,email,phone_number, password, role) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id", (name,username, email, phone_number,password,role, ))
#         user_id = cursor.fetchone()[0]
#         conn.commit()
#         return user_id
#     except Exception as e:
#         conn.rollback()
#         raise ValueError(f"Something went wrong: {str(e)}")
#     finally:
#         cursor.close()
#         conn.close()

# owner_ids = {}
# for owner in owners:
#     result = seed_owners(
#         owner["name"],
#         owner["username"],
#         owner["email"],
#         owner["phone_number"],
#         hash_password(owner["password"])
#     )
#     owner_ids[owner["username"]] = result["id"]


# def seed_restaurants(name, phone_number, address, trade_license_no, photo_url, cuisine_type,opening_time, owner_id):
#     conn = get_connection()
#     cursor = conn.cursor()

#     try:
#         cursor.execute("INSERT INTO restaurant (name, phone_number, address, trade_license_no, photo_url, cuisine_type,opening_time, owner_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id", (name, phone_number, address, trade_license_no, photo_url, cuisine_type,opening_time, owner_id, ))
#         restaurant_id = cursor.fetchone()[0]
#         conn.commit()
#         return restaurant_id
#     except Exception as e:
#         conn.rollback()
#         raise ValueError(f"Something went wrong: {str(e)}")
#     finally:
#         cursor.close()
#         conn.close()

# restaurant_ids = {}

# for restaurant in restaurants:
#     result = seed_restaurants(
#         restaurant["name"],
#         restaurant["phone_number"],
#         restaurant["address"],
#         restaurant["trade_license_no"],
#         restaurant["photo_url"],
#         restaurant["cuisine_type"],
#         restaurant["opening_time"],
#         owner_ids[restaurant["owner_username"]]
#     )
#     restaurant_ids[restaurant["name"]] = result

# def seed_menu_items(restaurant_id, name, price, portion_size, category, photo_url, is_available):
#     conn = get_connection()
#     cursor = conn.cursor()

#     try:
#         cursor.execute("INSERT INTO menu_items (restaurant_id, name, price, portion_size, category, photo_url, is_available) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id", (restaurant_id, name, price, portion_size, category, photo_url, is_available,))
#         item_id = cursor.fetchone()[0]
#         conn.commit()
#         return item_id
#     except Exception as e:
#         conn.rollback()
#         raise ValueError(f"Something went wrong: {str(e)}")
#     finally:
#         cursor.close()
#         conn.close()

# menu_item_ids = {}

# for restaurant_name, items in menu_items.items():
#     for item in items:
#         item_id = seed_menu_items(
#             restaurant_ids[restaurant_name],
#             item["name"],
#             item["price"],
#             item["portion_size"],
#             item["category"],
#             item["photo_url"],
#             item["is_available"]
#         )
#         menu_item_ids[item["name"]] = item_id


def seed_all():
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # 1. Insert owners
        owner_ids = {}
        for owner in owners:
            cursor.execute(
                "INSERT INTO users (name, username, email, phone_number, password, role) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id",
                (owner["name"], owner["username"], owner["email"], owner["phone_number"], hash_password(owner["password"]), "owner")
            )
            owner_ids[owner["username"]] = cursor.fetchone()[0]
        # 2. Insert restaurants
        restaurant_ids = {}

        for restaurant in restaurants:
            cursor.execute(
                "INSERT INTO restaurant (name, phone_number, address, trade_license_no, photo_url, cuisine_type, opening_time, owner_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id",
                (
                    restaurant["name"],
                    restaurant["phone_number"],
                    restaurant["address"],
                    restaurant["trade_license_no"],
                    restaurant["photo_url"],
                    restaurant["cuisine_type"],
                    restaurant["opening_time"],
                    owner_ids[restaurant["owner_username"]]
                )
            )
            restaurant_ids[restaurant["name"]] = cursor.fetchone()[0]
        # 3. Insert menu items

        menu_item_ids = {}

        for restaurant_name, items in menu_items.items():
            for item in items:
                cursor.execute(
                    "INSERT INTO menu_items (restaurant_id, name, price, portion_size, category, photo_url, is_available) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id",
                    (
                        restaurant_ids[restaurant_name],
                        item["name"],
                        item["price"],
                        item["portion_size"],
                        item["category"],
                        item["photo_url"],
                        item["is_available"]
                    )
                )
                menu_item_ids[item["name"]] = cursor.fetchone()[0]

        # 4. Insert students

        student_ids = {}

        for student in students:
            cursor.execute(
                "INSERT INTO users (name, username, email, phone_number, password, role) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id",
                (
                    student["name"],
                    student["username"],
                    student["email"],
                    student["phone_number"],
                    hash_password("student123"),
                    "student"
                )
            )
            user_id = cursor.fetchone()[0]

            cursor.execute(
                "INSERT INTO student_profiles (user_id, faculty) VALUES (%s,%s)",
                (user_id, random.choice(faculties))
            )

            student_ids[student["username"]] = user_id

        # 5. Generate events

        restaurant_id_list = list(restaurant_ids.values())
        menu_item_id_list = list(menu_item_ids.values())

        for student_id in student_ids.values():
            # each student prefers 2-3 restaurants
            preferred = random.sample(restaurant_id_list, k=2)
            
            for _ in range(random.randint(20, 30)):
                # 70% chance event is for a preferred restaurant
                if random.random() < 0.7:
                    r_id = random.choice(preferred)
                else:
                    r_id = random.choice(restaurant_id_list)
                    
                event_type = random.choice(["restaurant_viewed", "menu_viewed", "cart_added", "order_placed"])
                created_at = datetime.now() - timedelta(days=random.randint(0, 30))
                
                cursor.execute(
                    "INSERT INTO events (student_id, event_type, restaurant_id, created_at) VALUES (%s,%s,%s,%s)",
                    (student_id, event_type, r_id, created_at)
                )
        conn.commit()
        print("Seeding complete")
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    seed_all()
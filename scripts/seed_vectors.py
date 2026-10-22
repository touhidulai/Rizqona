from ai_engine.embeddings import embed_text
from ai_engine.vector_store import store_embeddings
from database.connection import get_connection
from psycopg2.extras import RealDictCursor

conn = get_connection()
cursor = conn.cursor(cursor_factory = RealDictCursor)
cursor.execute("SELECT * FROM menu_items")
items = cursor.fetchall()
total = len(items)

for index, item in enumerate (items):
    
    content = f"{item['name']} {item['category']} {item['portion_size']} RM{item['price']}"
    store_embeddings(item['id'],content)
    print(f"Embedded {index + 1}/{total}: {item['name']}")

cursor.close()
conn.close()

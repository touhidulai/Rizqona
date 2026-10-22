from database.connection import get_connection
from ai_engine.vector_store import search_similar
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    )   

def ask(query: str)->str:

    conn = get_connection()
    cursor = conn.cursor()

    try:
        results = search_similar(query)
        ids = tuple([row[0] for row in results])
        cursor.execute("SELECT mi.name, mi.price, r.name as restaurant_name FROM menu_items mi JOIN restaurant r ON mi.restaurant_id = r.id WHERE mi.id IN %s", (ids,))
        menu_items = cursor.fetchall()
        context = "\n".join([f"{item[2]}: {item[0]} - RM{item[1]}" for item in menu_items])
        prompt = f"""You are a campus food assistant for Universiti Malaya.
        Based on these menu items from Rizqona:
        {context}

        Answer this student query: {query}
        Be helpful and mention specific dishes, prices and restaurants."""

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        raise ValueError(f"Something went wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()    
    







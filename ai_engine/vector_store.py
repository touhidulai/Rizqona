from database.connection import get_connection
from ai_engine.embeddings import embed_text

def store_embeddings(menu_item_id, text):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        embedded = embed_text(text)
        cursor.execute("INSERT INTO menu_item_embeddings (menu_item_id, embedding, content) VALUES (%s,%s,%s)", (menu_item_id, embedded, text,))
        conn.commit()
        return "Saved embedding into DB"
    except Exception as e:
        conn.rollback()
        raise ValueError(f"Failed to add embeddings: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def search_similar(query_text: str, limit = 5):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        query_embedded = embed_text(query_text)
        cursor.execute("SELECT menu_item_id, content FROM menu_item_embeddings ORDER BY embedding <=> %s::vector LIMIT %s",(str(query_embedded),limit))
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise ValueError(f"Failed to find similar: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def delete_embedding(menu_item_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM menu_item_embeddings WHERE menu_item_id = %s", (menu_item_id,))
        conn.commit()
        return f"Embedding Deleted for Menu Item: {menu_item_id}"
    except Exception as e:
        raise ValueError(f"Failed to delete Menu Item Embeddings: {str(e)}")
    finally:
        cursor.close()
        conn.close()


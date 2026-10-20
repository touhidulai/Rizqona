from database.connection import get_connection
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()

def get_restaurant_features():

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, cuisine_type FROM restaurant")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=["restaurant_id", "cuisine_type"])
        return df
    except Exception as e:
        raise ValueError(f"Something is wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()


def get_student_preferences(student_id):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT restaurant_id, COUNT(*) as interaction_count FROM events WHERE student_id = %s AND restaurant_id IS NOT NULL GROUP BY restaurant_id ORDER BY interaction_count DESC", (student_id,))
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=["restaurant_id", "interaction_count"])
        return df
    except Exception as e:
        raise ValueError(f"Something is wrong: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def build_similarity_matrix():
    df = get_restaurant_features()
    tfidf_matrix = vectorizer.fit_transform(df["cuisine_type"])
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix, df

def get_recommendations(student_id, top_n=5):
    # Step 1: Get what student already viewed
    preferences_df = get_student_preferences(student_id)
    already_viewed = set(preferences_df["restaurant_id"].tolist())
    
    # Step 2: Get similarity matrix
    similarity_matrix, restaurant_df = build_similarity_matrix()
    
    # Step 3: Get student's top restaurant
    if preferences_df.empty:
        return []
    top_restaurant_id = preferences_df.iloc[0]["restaurant_id"]
    
    # Step 4: Find its position in the matrix
    restaurant_idx = restaurant_df[restaurant_df["restaurant_id"] == top_restaurant_id].index[0]
    
    # Step 5: Get similarity scores
    similarity_scores = similarity_matrix[restaurant_idx]
    
    # Step 6: Sort and filter
    similar = sorted(enumerate(similarity_scores), key=lambda x: x[1], reverse=True)
    
    recommendations = []
    for idx, score in similar:
        r_id = restaurant_df.iloc[idx]["restaurant_id"]
        if r_id not in already_viewed:
            recommendations.append(int(r_id))
        if len(recommendations) >= top_n:
            break
    
    return recommendations

from fastapi import APIRouter, HTTPException, Depends
from services.auth_service import get_current_user
from ml_engine.recommendation import get_recommendations, get_student_preferences
from database.restaurant_repository import get_restaurants_by_ids,get_restaurant_by_id


router = APIRouter()

@router.get("/recommendations")
def get_recommendation_endpoint(current_user: int = Depends(get_current_user)):
    restaurant_ids = get_recommendations(current_user)
    return get_restaurants_by_ids(restaurant_ids)

@router.get("/recommendations/explain")
def recommendation_explain_endpoint(current_user: int = Depends(get_current_user)):
    top_viewed = get_student_preferences(current_user)
    top_id = int(top_viewed.iloc[0]["restaurant_id"])
    top_cuisine = get_restaurant_by_id(top_id)
    restaurant_ids = get_recommendations(current_user)

    return {
        "reasons": f"Recommended because you frequently visit {top_cuisine['cuisine_type']} cuisine restaurants",
        "recommendations": get_restaurants_by_ids(restaurant_ids)
    }
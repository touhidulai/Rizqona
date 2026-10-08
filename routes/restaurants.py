from fastapi import APIRouter, HTTPException, Depends
from database.restaurant_repository import get_all_restaurants,create_restaurant,get_restaurant_by_id,create_menu_item, update_menu_item_availability, get_full_menu_by_restaurant_id
from models.restaurants import RestaurantCreate, MenuItemCreate, AvailabilityUpdate, MenuItemResponse
from services.auth_service import get_current_user
from database.event_repo import create_event

router = APIRouter()

@router.get("/restaurants")
def all_restaurants_endpoint():
    restaurants = get_all_restaurants()
    return restaurants

@router.get("/restaurants/{id}")
def restaurant_byid_endpoint(id: int, current_user: int = Depends(get_current_user)):
    restaurant = get_restaurant_by_id(id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    event_type = "restaurant_viewed"
    create_event(current_user,event_type,id)
    return restaurant

@router.get("/restaurants/{id}/full_menu")
def get_restaurant_full_menu(id: int, current_user: int = Depends(get_current_user)):
    full_menu = get_full_menu_by_restaurant_id(id)

    if full_menu is None:
        raise HTTPException(status_code=404, detail="Restaurant's menu not found")
    event_type = "menu_viewed"
    create_event(current_user, event_type, id, None)
    return full_menu

@router.post("/restaurants")
def create_restaurant_endpoint(restaurant: RestaurantCreate, current_user: int = Depends(get_current_user)):

    restaurant_id = create_restaurant(restaurant.name, restaurant.phone_number, restaurant.address, restaurant.trade_license_no,restaurant.photo_url,restaurant.cuisine_type,restaurant.opening_time)
    return restaurant_id

@router.post("/restaurants/{id}/menu-items")
def create_menu_item_endpoint(id: int, menu: MenuItemCreate, current_user: int = Depends(get_current_user)):
    menu_id = create_menu_item(id, menu.name, menu.price, menu.portion_size, menu.category, menu.photo_url, menu.is_available)
    return menu_id

@router.patch("/restaurants/{id}/menu-items/{item_id}")
def change_item_availability_endpoint(item_id: int, availability: AvailabilityUpdate, current_user: int = Depends(get_current_user)):
    return update_menu_item_availability(item_id, availability.is_available)

from fastapi import APIRouter, HTTPException
from database.repository import get_all_restaurants,create_restaurant,get_restaurant_by_id,create_menu_item, update_menu_item_availability
from models.restaurants import RestaurantCreate, MenuItemCreate, AvailabilityUpdate

router = APIRouter()

@router.get("/restaurants")
def all_restaurants_endpoint():
    restaurants = get_all_restaurants()
    return restaurants

@router.get("/restaurants/{id}")
def restaurant_byid_endpoint(id: int):
    restaurant = get_restaurant_by_id(id)
    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

@router.post("/restaurants")
def create_restaurant_endpoint(restaurant: RestaurantCreate):
    restaurant_id = create_restaurant(restaurant.name, restaurant.phone_number, restaurant.address, restaurant.trade_license_no,restaurant.photo_url,restaurant.cuisine_type,restaurant.opening_time)
    return restaurant_id

@router.post("/restaurants/{id}/menu-items")
def create_menu_item_endpoint(id: int, menu: MenuItemCreate):
    menu_id = create_menu_item(id, menu.name, menu.price, menu.portion_size, menu.category, menu.photo_url, menu.is_available)
    return menu_id

@router.patch("/restaurants/{id}/menu-items/{item_id}")
def change_item_availability_endpoint(item_id: int, availability: AvailabilityUpdate):
    return update_menu_item_availability(item_id, availability.is_available)


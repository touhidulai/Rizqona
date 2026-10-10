from fastapi import APIRouter, HTTPException, Depends
from services.auth_service import get_current_user
from database.event_repo import create_event
from database.order_repo import add_to_cart, get_cart, place_order, get_orders, get_restaurant_orders, update_order_status
from database.restaurant_repository import get_restaurant_by_owner_id
from database.event_repo import create_event

router = APIRouter()

@router.post("/cart")
def add_item_to_cart_endpoint(menu_item_id: int, quantity: int, current_user: int = Depends(get_current_user)):
    cart = add_to_cart(current_user, menu_item_id, quantity)
    event_type = "cart_added"
    create_event(current_user,event_type,None,menu_item_id)
    return cart

@router.get("/cart")
def view_cart_endpoint(current_user: int = Depends(get_current_user)):
    return get_cart(current_user)


@router.post("/orders")
def place_order_endpoint(current_user: int = Depends(get_current_user)):
    orders = place_order(current_user)
    event_type = "order_placed"
    create_event(current_user,event_type,None,None)
    return orders

@router.get("/orders")
def view_orders_endpoint(current_user: int = Depends(get_current_user)):
    return get_orders(current_user)

@router.get("/orders/restaurant")
def view_restaurant_orders(current_user: int = Depends(get_current_user)):
    restaurant_id = get_restaurant_by_owner_id(current_user)
    orders = get_restaurant_orders(restaurant_id)

    if len(orders["Order Items"]) == 0:
        raise HTTPException(status_code = 404, detail = "Orders are Empty")

    return orders

@router.patch("/orders/{id}/status")
def update_order_status_endpoint(id: int, status: str,current_user: int = Depends(get_current_user)):

    return update_order_status (id, status)

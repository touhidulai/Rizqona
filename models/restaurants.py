from pydantic import BaseModel
from datetime import time
from typing import Optional
from decimal import Decimal

class RestaurantCreate(BaseModel):

    name: str
    phone_number: str
    address: str
    trade_license_no: str
    photo_url: str
    cuisine_type: str
    opening_time: time

class RestaurantResponse(RestaurantCreate):

    id: int

class MenuItemCreate(BaseModel):
    name: str
    price: Decimal
    portion_size: Optional[str] = None
    category: str
    photo_url: str
    is_available: bool

class MenuItemResponse(MenuItemCreate):
    id: int

class AvailabilityUpdate(BaseModel):
    is_available: bool

class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    cuisine_type: Optional[str] = None
    opening_time: Optional[time] = None

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[Decimal] = None
    portion_size: Optional[str] = None
    category: Optional[str] = None
from pydantic import BaseModel
from datetime import time

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
    
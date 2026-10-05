from typing import Optional

from pydantic import BaseModel, Field


class RestaurantCreate(BaseModel):
    name: str
    location: str
    phone: str


class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    phone: Optional[str] = None


class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    password: str = Field(..., min_length=1, max_length=72)
    
class UserLogin(BaseModel):
    email: str
    password: str

class FoodCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    restaurant_id: int

class FoodUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None

class CartItemCreate(BaseModel):
    food_id: int
    quantity: int = Field(..., gt=0)


class CartItemUpdate(BaseModel):
    quantity: int = Field(..., gt=0)
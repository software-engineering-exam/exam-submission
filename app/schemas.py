from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category: str
    in_stock_quantity: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    category: Optional[str]
    in_stock_quantity: Optional[int]


class ProductOut(ProductBase):
    id: int
    created_date: datetime
    last_updated_date: datetime


    class Config:
        orm_mode = True


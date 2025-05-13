from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from .database import Base


class Product(Base):
    __tablename__ = "products"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    in_stock_quantity = Column(Integer)
    created_date = Column(DateTime, default=datetime.utcnow)
    last_updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

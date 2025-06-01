from typing import Optional
from pydantic import BaseModel
from datetime import date
from sqlalchemy import Column, Integer, Float, String, Date

from persistence.db import Base


class ExpenseModel(Base):
    __tablename__: str = 'expense'

    id: int = Column(Integer, primary_key=True)
    description: str = Column(String, nullable=False)
    amount: float = Column(Float, nullable=False)
    category: str = Column(String, nullable=False)
    account: str = Column(String, nullable=False)
    created_date: date = Column(Date, nullable=False)


class ExpenseSchema(BaseModel):
    id: Optional[int]
    description: str
    amount: float
    category: str
    account: str
    created_date: Optional[date]

    class Config:
        from_attributes: bool = True

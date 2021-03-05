from datetime import date, datetime
from typing import List
from pydantic import BaseModel


class Price(BaseModel):
    id: int
    created_at: datetime
    price: str

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QuoteModel(BaseModel):
    id: Optional[int] = None
    enquiry_id: int
    amount: float
    status: str
    category_id: int
    quote_type: str
    quote_details: str
    quote_title: str
    timestamp: Optional[datetime] = None

    class Config:
        orm_mode = True

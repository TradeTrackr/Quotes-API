from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CalendarModel(BaseModel):
    id: Optional[int] = None
    quote_id: Optional[int] = None
    scheduled_start_date_and_time: Optional[datetime] = None
    scheduled_end_date_and_time: Optional[datetime] = None
    event_type: Optional[str] = None
    company_id: str
    all_day: bool
    event_status: str
    event_title: str
    notes: str
    timestamp: Optional[datetime] = None

    class Config:
        orm_mode = True

class QuoteModel(BaseModel):
    id: Optional[int] = None
    enquiry_id: int
    amount: float
    status: str
    category_id: int
    company_id: str
    quote_type: str
    quote_details: str
    quote_title: str
    timestamp: Optional[datetime] = None
    calendar_events: List[CalendarModel] = []

    class Config:
        orm_mode = True

class IncomingModel(BaseModel):
    enquiry_id: Optional[int] = None
    quote_title: str
    quote_details: str
    amount: Optional[float] = None
    category_id: Optional[int] = None
    status: str
    all_day: bool
    company_id: str
    quote_type: Optional[str] = None
    scheduled_start_date_and_time: Optional[str] = None
    scheduled_end_date_and_time: Optional[str] = None
    timestamp: Optional[datetime] = None


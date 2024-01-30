from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Quote(Base):
    __tablename__ = 'quote'

    id = Column(Integer, primary_key=True, index=True)
    enquiry_id = Column(Integer, index=True)
    amount = Column(Float, index=True)
    status = Column(String, index=True)
    quote_type = Column(String, index=True)
    company_id = Column(String, index=True)
    category_id = Column(Integer, index=True)
    quote_details = Column(String, index=True)
    quote_title = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, nullable=True)
    calendar_events = relationship('Calendar', order_by='Calendar.scheduled_start_date_and_time', back_populates='quote', lazy="selectin")

class Calendar(Base):
    __tablename__ = 'calendar'

    id = Column(Integer, primary_key=True, index=True)
    quote_id = Column(Integer, ForeignKey('quote.id'), nullable=True)
    scheduled_start_date_and_time = Column(DateTime, nullable=True)
    scheduled_end_date_and_time = Column(DateTime, nullable=True)
    event_type = Column(String, nullable=True)
    company_id = Column(String, index=True)
    all_day = Column(Boolean, index=True)
    event_status = Column(String, index=True)
    event_title = Column(String, index=True)
    notes = Column(String, nullable=True)
    quote = relationship('Quote', back_populates='calendar_events')
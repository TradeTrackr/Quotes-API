from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime

Base = declarative_base()

class Quote(Base):
    __tablename__ = 'quote'

    id = Column(Integer, primary_key=True, index=True)
    enquiry_id = Column(Integer, index=True)
    amount = Column(Float, index=True)
    status = Column(String, index=True)
    category_id = Column(Integer, index=True)
    quote_details = Column(String, index=True)
    quote_title = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow(), nullable=True)
    calendar_events = relationship('Calendar', order_by='Calendar.scheduled_date', back_populates='quote')

class Calendar(Base):
    __tablename__ = 'calendar'

    id = Column(Integer, primary_key=True, index=True)
    quote_id = Column(Integer, ForeignKey('quote.id'), nullable=False)
    scheduled_date = Column(DateTime, nullable=False)
    event_type = Column(String, nullable=False)
    event_status = Column(String, index=True)
    notes = Column(String, nullable=True)
    # Relationship to the Quote model
    quote = relationship('Quote', back_populates='calendar_events')

import imp
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utilities.db import get_db
from app.utilities.crud import (
        new_calendar_event,
        get_calendar_for_company_with_quotes,
        new_trader,
        get_quotes_for_enquiry
)
from app.utilities.authentication import Authentication
from app.validation_models import QuoteModel, IncomingModel, CalendarModel
import datetime

quote_route = APIRouter()

@quote_route.get("/get_quote/{id}", status_code=200)
async def get_quotes(id: int, user=Depends(Authentication().validate_token), db: AsyncSession = Depends(get_db)) -> dict:
    quote = await get_quotes_for_enquiry(db, id)
    if quote is None:
        raise HTTPException(status_code=404, detail="No quotes found")
    return {"quote": quote}

@quote_route.get("/get_quotes/{id}", status_code=200)
async def get_enquiry_quotes(id: int, user=Depends(Authentication().validate_token), db: AsyncSession = Depends(get_db)) -> dict:
    quote = await get_quotes_for_enquiry(db, id)
    if quote is None:
        raise HTTPException(status_code=404, detail="No quotes found for enquiry")
    return {"quotes": quote}

@quote_route.get("/get_company_quotes/{id}", status_code=200)
async def get_company_quotes(id: str, user=Depends(Authentication().validate_token), db: AsyncSession = Depends(get_db)) -> dict:
    quote = await get_calendar_for_company_with_quotes(db, id)
    if quote is None:
        raise HTTPException(status_code=404, detail="No quotes found for company")
    return {"quotes": quote}

@quote_route.post("/new", response_model=QuoteModel)
async def create_quote(incoming_quote: IncomingModel, user=Depends(Authentication().validate_token), db: AsyncSession = Depends(get_db)) -> dict:
   
    quote_model = QuoteModel(
        enquiry_id=incoming_quote.enquiry_id,
        amount=incoming_quote.amount,
        status=incoming_quote.status,
        quote_type=incoming_quote.quote_type,
        category_id=incoming_quote.category_id,
        quote_details=incoming_quote.quote_details,
        quote_title=incoming_quote.quote_title,
        company_id=incoming_quote.company_id,
        # other fields as necessary
    )

    new_quote = await new_trader(db, quote_model)

    calendar_model = CalendarModel(
        scheduled_start_date_and_time=incoming_quote.scheduled_start_date_and_time,
        scheduled_end_date_and_time=incoming_quote.scheduled_end_date_and_time,
        event_type=incoming_quote.quote_type,
        company_id=incoming_quote.company_id,
        event_status=incoming_quote.status,
        notes=incoming_quote.quote_details,
        quote_id = new_quote.id,
        event_title = incoming_quote.quote_title
    )

    new_calendar = await new_calendar_event(db, calendar_model)
    new_quote.calendar_events.append(new_calendar)

    return new_quote
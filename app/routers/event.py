import imp
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utilities.db import get_db
from app.utilities.crud import new_calendar_event
from app.utilities.authentication import Authentication
from app.validation_models import IncomingModel, CalendarModel
import datetime

event_route = APIRouter()

# @event_route.get("/get_event/{id}", status_code=200)
# async def get_event(id: int, user=Depends(Authentication().validate_token), db: AsyncSession = Depends(get_db)) -> dict:
#     quote = await get_quotes_for_enquiry(db, id)
#     if quote is None:
#         raise HTTPException(status_code=404, detail="No quotes found")
#     return {"quote": quote}

# @event_route.get("/get_events/{id}", status_code=200)
# async def get_events(id: int, user=Depends(Authentication().validate_token), db: AsyncSession = Depends(get_db)) -> dict:
#     quote = await get_quotes_for_enquiry(db, id)
#     if quote is None:
#         raise HTTPException(status_code=404, detail="No quotes found for enquiry")
#     return {"quotes": quote}

# @event_route.get("/get_company_events{id}", status_code=200)
# async def get_company_events(id: str, user=Depends(Authentication().validate_token), db: AsyncSession = Depends(get_db)) -> dict:
#     quote = await get_calendar_for_company_with_quotes(db, id)
#     if quote is None:
#         raise HTTPException(status_code=404, detail="No quotes found for company")
#     return {"quotes": quote}

@event_route.post("/new", response_model=CalendarModel)
async def create_quote(incoming_quote: IncomingModel, user=Depends(Authentication().validate_token), db: AsyncSession = Depends(get_db)) -> dict:

    calendar_model = CalendarModel(
        scheduled_start_date_and_time=incoming_quote.scheduled_start_date_and_time,
        scheduled_end_date_and_time=incoming_quote.scheduled_end_date_and_time,
        event_type=incoming_quote.quote_type,
        company_id=incoming_quote.company_id,
        event_status=incoming_quote.status,
        notes=incoming_quote.quote_details,
        event_title = incoming_quote.quote_title,
        all_day = incoming_quote.all_day
    )

    new_calendar = await new_calendar_event(db, calendar_model)

    return new_calendar
# crud.py
from calendar import Calendar
from sqlalchemy.ext.asyncio import AsyncSession
from app import models
from app.validation_models import QuoteModel, CalendarModel
from sqlalchemy import select
from datetime import datetime
from sqlalchemy.orm import selectinload
from fastapi import HTTPException


async def get_quote_by_id(db: AsyncSession, quote_id: int):
    return await db.get(models.Quote, quote_id)

async def get_quotes_for_enquiry(db: AsyncSession, enquiry_id: int):
    result = await db.execute(select(models.Quote).where(models.Quote.enquiry_id == enquiry_id))
    return result.scalars().all()

async def get_calendar_for_company(db: AsyncSession, company_id: str):
    result = await db.execute(select(models.Calendar).where(models.Calendar.company_id == company_id))
    return result.scalars().all()

async def get_calendar_for_company_with_quotes(db: AsyncSession, company_id: str):
    result = await db.execute(
        select(models.Calendar)
        .options(selectinload(models.Calendar.quote))
        .where(models.Calendar.company_id == company_id)
    )
    return result.scalars().all()

async def update_calendar_event(db: AsyncSession, calendar_id: int, calendar: CalendarModel):

    query = select(models.Calendar).where(models.Calendar.id == calendar_id)
    result = await db.execute(query)
    calendar_event = result.scalar_one_or_none()

    if not calendar_event:
        raise HTTPException(status_code=404, detail="Calendar event not found")

    # Update the fields
    for var, value in vars(calendar).items():
        setattr(calendar_event, var, value) if value else None

    db.add(calendar_event)
    await db.commit()
    return calendar_event

async def new_calendar_event(db: AsyncSession, calendar: CalendarModel):

    if isinstance(calendar.scheduled_start_date_and_time, str):
        calendar.scheduled_start_date_and_time = datetime.strptime(calendar.scheduled_start_date_and_time, '%Y-%m-%dT%H:%M')

    if isinstance(calendar.scheduled_end_date_and_time, str):
        calendar.scheduled_end_date_and_time = datetime.strptime(calendar.scheduled_end_date_and_time, '%Y-%m-%dT%H:%M')

    db_quote = models.Calendar(
                quote_id=calendar.quote_id,
                scheduled_start_date_and_time=calendar.scheduled_start_date_and_time,
                scheduled_end_date_and_time=calendar.scheduled_end_date_and_time,
                event_type=calendar.event_type,
                company_id=calendar.company_id,
                all_day=calendar.all_day,
                event_status=calendar.event_status,
                notes=calendar.notes,
                event_title=calendar.event_title
    )

    db.add(db_quote)
    await db.commit()
    await db.refresh(db_quote)
    return db_quote

async def new_trader(db: AsyncSession, quote: QuoteModel):

    db_quote = models.Quote(
                enquiry_id=quote.enquiry_id,
                amount=quote.amount,
                status=quote.status,
                quote_details=quote.quote_details,
                quote_type=quote.quote_type,
                category_id=quote.category_id,
                quote_title=quote.quote_title,
                company_id=quote.company_id
    )

    db.add(db_quote)
    await db.commit()
    await db.refresh(db_quote)
    return db_quote

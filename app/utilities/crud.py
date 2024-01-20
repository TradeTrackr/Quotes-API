# crud.py
from sqlalchemy.orm import Session
from app import models
from app.validation_models import QuoteModel
from sqlalchemy import select


async def get_quote_by_id(db: Session, quote_id: int):
    return await db.get(models.Quote, quote_id)


async def get_quotes_for_enquiry(db: Session, enquiry_id: int):
    result = await db.execute(select(models.Quote).where(models.Quote.enquiry_id == enquiry_id))
    return result.scalars().all()


async def new_trader(db: Session, quote: QuoteModel):

    db_quote = models.Quote(
                enquiry_id=quote.enquiry_id,
                amount=quote.amount,
                status=quote.status,
                quote_details=quote.quote_details,
                quote_type=quote.quote_type,
                category_id=quote.category_id,
                quote_title=quote.quote_title
    )

    db.add(db_quote)
    await db.commit()
    await db.refresh(db_quote)
    return db_quote

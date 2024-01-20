import imp
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utilities.db import get_db
from app.utilities.crud import get_quote_by_id, new_trader, get_quotes_for_enquiry
from app.utilities.authentication import Authentication
from app.validation_models import QuoteModel
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

@quote_route.post("/new", response_model=QuoteModel)
async def create_quote(quote: QuoteModel, user=Depends(Authentication().validate_token), db: AsyncSession = Depends(get_db)) -> dict:
    new_quote = await new_trader(db, quote)
    return QuoteModel(
        id=new_quote.id,
        enquiry_id=new_quote.enquiry_id,
        amount=new_quote.amount,
        status=new_quote.status,
        quote_type=new_quote.quote_type,
        category_id=new_quote.category_id,
        quote_details=new_quote.quote_details,
        quote_title=new_quote.quote_title
    )
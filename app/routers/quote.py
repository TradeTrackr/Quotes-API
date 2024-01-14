import imp
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utilities.db import get_db
from app.utilities.crud import get_quote_by_id, new_trader
from app.utilities.authentication import Authentication
from app.validation_models import QuoteModel
import datetime

quote_route = APIRouter()

# get trader by id
@quote_route.get("/get_quote/{id}", status_code=200)
async def get_trader(id: int, user=Depends(Authentication.validate_token), db: AsyncSession = Depends(get_db)) -> dict:
    quote = await get_quote_by_id(db, id)
    if quote is None:
        raise HTTPException(status_code=404, detail="Trader not found")
    return {"trader": quote}

@quote_route.post("/new", response_model=QuoteModel)
async def create_quote(quote: QuoteModel, user=Depends(Authentication.validate_token), db: AsyncSession = Depends(get_db)) -> dict:
    new_quote = await new_trader(db, quote)
    return {"message": "Quote created successfully.", "id": new_quote.id}

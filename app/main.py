from fastapi import FastAPI
from app.models import Quote
from .routers.quote import quote_route

app = FastAPI()

app.include_router(quote_route, prefix="/quote")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
from fastapi import FastAPI
from app.models import Quote
from .routers.quote import quote_route
from .routers.event import event_route

app = FastAPI()

app.include_router(quote_route, prefix="/quote")
app.include_router(event_route, prefix="/event")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
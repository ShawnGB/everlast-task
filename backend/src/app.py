from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.leads.router import router as leads_router
from src.contact.router import router as contact_router


@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(leads_router)
app.include_router(contact_router)

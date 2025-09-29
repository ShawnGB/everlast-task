from contextlib import asynccontextmanager
from fastapi import FastAPI

from src.leads.router import router as leads_router
from src.contact.router import router as contact_router

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # dein Frontend-Dev-Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(leads_router)
app.include_router(contact_router)

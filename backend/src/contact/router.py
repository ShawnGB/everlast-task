from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.connection import get_db
from src.contact import schemas, service

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.post("/", response_model=schemas.ContactRead, status_code=201)
async def create_contact(
    contact_in: schemas.ContactCreate,
    db: AsyncSession = Depends(get_db),
):
    return await service.create_contact(db, contact_in)


@router.get("/{contact_id}", response_model=schemas.ContactRead)
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_contact(db, contact_id)


@router.get("/", response_model=List[schemas.ContactRead])
async def list_contacts(db: AsyncSession = Depends(get_db)):
    return await service.list_contacts(db)


@router.patch("/{contact_id}", response_model=schemas.ContactRead)
async def update_contact(
    contact_id: int,
    contact_update: schemas.ContactUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await service.update_contact(db, contact_id, contact_update)


@router.delete("/{contact_id}", status_code=204)
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    await service.delete_contact(db, contact_id)
    return None

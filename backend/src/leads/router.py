from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.connection import get_db
from src.leads import schemas, service

router = APIRouter(prefix="/leads", tags=["leads"])


@router.post("/", response_model=schemas.LeadRead, status_code=201)
async def create_lead(
    lead_in: schemas.LeadCreate,
    db: AsyncSession = Depends(get_db),
):
    return await service.create_lead(db, lead_in)


@router.get("/{lead_id}", response_model=schemas.LeadRead)
async def get_lead(lead_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_lead(db, lead_id)


@router.get("/", response_model=List[schemas.LeadRead])
async def list_leads(db: AsyncSession = Depends(get_db)):
    return await service.list_leads(db)


@router.patch("/{lead_id}", response_model=schemas.LeadRead)
async def update_lead(
    lead_id: int,
    lead_update: schemas.LeadUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await service.update_lead(db, lead_id, lead_update)


@router.delete("/{lead_id}", status_code=204)
async def delete_lead(lead_id: int, db: AsyncSession = Depends(get_db)):
    await service.delete_lead(db, lead_id)
    return None

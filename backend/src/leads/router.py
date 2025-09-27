from typing import List, Optional
from fastapi import APIRouter, Depends, Query
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


@router.get("/", response_model=List[schemas.LeadRead])
async def list_leads(
    db: AsyncSession = Depends(get_db),
    q: Optional[str] = Query(default=None, description="Search by name or domain"),
    status: Optional[schemas.LeadStatus] = Query(default=None),
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return await service.list_leads(db, q=q, status=status, limit=limit, offset=offset)


@router.get("/{lead_id}", response_model=schemas.LeadRead)
async def get_lead(
    lead_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await service.get_lead(db, lead_id)


@router.put("/{lead_id}", response_model=schemas.LeadRead)
async def update_lead(
    lead_id: int,
    lead_update: schemas.LeadUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await service.update_lead(db, lead_id, lead_update)


@router.delete("/{lead_id}", status_code=204)
async def delete_lead(
    lead_id: int,
    db: AsyncSession = Depends(get_db),
):
    await service.delete_lead(db, lead_id)
    return None


# Bonus Endpoint: nur Status ändern
@router.post("/{lead_id}/status", response_model=schemas.LeadRead)
async def update_status(
    lead_id: int,
    status: schemas.LeadStatus,
    db: AsyncSession = Depends(get_db),
):
    return await service.update_lead(db, lead_id, schemas.LeadUpdate(status=status))

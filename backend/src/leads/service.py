from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from src.leads import models, schemas


async def create_lead(db: AsyncSession, lead_in: schemas.LeadCreate) -> models.Lead:
    """
    Create a new lead.
    """
    new_lead = models.Lead(**lead_in.model_dump())
    db.add(new_lead)
    await db.commit()
    await db.refresh(new_lead)
    return new_lead


async def get_lead(db: AsyncSession, lead_id: int) -> models.Lead:
    """
    Retrieve a lead by ID or raise 404 if not found.
    """
    result = await db.execute(select(models.Lead).where(models.Lead.id == lead_id))
    lead = result.scalar_one_or_none()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead


async def list_leads(db: AsyncSession) -> List[models.Lead]:
    """
    Return a list of all leads.
    """
    result = await db.execute(select(models.Lead))
    return list(result.scalars().all())


async def update_lead(
    db: AsyncSession, lead_id: int, lead_update: schemas.LeadUpdate
) -> models.Lead:
    """
    Update an existing lead.
    """
    result = await db.execute(select(models.Lead).where(models.Lead.id == lead_id))
    db_lead = result.scalar_one_or_none()
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    for field, value in lead_update.model_dump(exclude_unset=True).items():
        setattr(db_lead, field, value)

    await db.commit()
    await db.refresh(db_lead)
    return db_lead


async def delete_lead(db: AsyncSession, lead_id: int) -> None:
    """
    Delete a lead by ID. Raises 404 if not found.
    """
    result = await db.execute(select(models.Lead).where(models.Lead.id == lead_id))
    db_lead = result.scalar_one_or_none()
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    await db.delete(db_lead)
    await db.commit()

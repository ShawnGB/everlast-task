from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from fastapi import HTTPException

from src.leads import models, schemas

from src.contact import models as contact_models


async def create_lead(db: AsyncSession, lead_in: schemas.LeadCreate) -> models.Lead:
    primary_contact_id = lead_in.primary_contact_id

    # Falls ein neuer Contact mitgegeben ist → erstellen
    if lead_in.primary_contact:
        contact_data = lead_in.primary_contact

        new_contact = contact_models.Contact(
            first_name=contact_data.first_name,
            last_name=contact_data.last_name,
        )
        db.add(new_contact)
        await db.flush()  # ID vom Kontakt verfügbar machen

        # Email(s) anlegen
        if contact_data.emails:
            for email in contact_data.emails:
                new_email = contact_models.ContactEmail(
                    contact_id=new_contact.id,
                    value=email.value,
                    is_primary=email.is_primary,
                )
                db.add(new_email)

        primary_contact_id = new_contact.id

    # Lead selbst erstellen
    new_lead = models.Lead(
        name=lead_in.name,
        domain=lead_in.domain,
        status=lead_in.status,
        primary_contact_id=primary_contact_id,
    )
    db.add(new_lead)

    await db.commit()
    await db.refresh(new_lead)
    return new_lead


async def get_lead(db: AsyncSession, lead_id: int) -> models.Lead:
    result = await db.execute(select(models.Lead).where(models.Lead.id == lead_id))
    lead = result.scalar_one_or_none()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead


async def list_leads(
    db: AsyncSession,
    q: Optional[str] = None,
    status: Optional[schemas.LeadStatus] = None,
    limit: int = 20,
    offset: int = 0,
) -> List[models.Lead]:
    stmt = select(models.Lead)

    if status:
        stmt = stmt.where(models.Lead.status == status)

    if q:
        stmt = stmt.where(
            or_(
                models.Lead.name.ilike(f"%{q}%"),
                models.Lead.domain.ilike(f"%{q}%"),
            )
        )

    stmt = stmt.limit(limit).offset(offset)
    result = await db.execute(stmt)
    return list(result.scalars().all())


async def update_lead(
    db: AsyncSession, lead_id: int, lead_update: schemas.LeadUpdate
) -> models.Lead:
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
    result = await db.execute(select(models.Lead).where(models.Lead.id == lead_id))
    db_lead = result.scalar_one_or_none()
    if not db_lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    await db.delete(db_lead)
    await db.commit()

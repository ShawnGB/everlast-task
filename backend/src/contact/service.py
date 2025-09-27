from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from src.contact import models, schemas


async def create_contact(
    db: AsyncSession, contact_in: schemas.ContactCreate
) -> models.Contact:
    """
    Create a new contact with optional email addresses.
    """
    new_contact = models.Contact(
        first_name=contact_in.first_name,
        last_name=contact_in.last_name,
    )
    db.add(new_contact)
    await db.flush()  # ensures `new_contact.id` is available

    if contact_in.emails:
        for email in contact_in.emails:
            new_email = models.ContactEmail(
                contact_id=new_contact.id,
                value=email.value,
                is_primary=email.is_primary,
            )
            db.add(new_email)

    await db.commit()
    await db.refresh(new_contact)
    return new_contact


async def get_contact(db: AsyncSession, contact_id: int) -> models.Contact:
    """
    Retrieve a contact by ID or raise 404 if not found.
    """
    result = await db.execute(
        select(models.Contact).where(models.Contact.id == contact_id)
    )
    contact = result.scalar_one_or_none()
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


async def list_contacts(db: AsyncSession) -> List[models.Contact]:
    """
    Return a list of all contacts.
    """
    result = await db.execute(select(models.Contact))
    return list(result.scalars().all())


async def update_contact(
    db: AsyncSession, contact_id: int, contact_update: schemas.ContactUpdate
) -> models.Contact:
    """
    Update a contact and optionally replace email addresses.
    """
    result = await db.execute(
        select(models.Contact).where(models.Contact.id == contact_id)
    )
    db_contact = result.scalar_one_or_none()
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    for field, value in contact_update.model_dump(exclude_unset=True).items():
        if field != "emails":
            setattr(db_contact, field, value)

    if contact_update.emails is not None:
        for email in db_contact.contact_emails:
            await db.delete(email)

        for email_in in contact_update.emails:
            new_email = models.ContactEmail(
                contact_id=db_contact.id,
                value=email_in.value,
                is_primary=email_in.is_primary or False,
            )
            db.add(new_email)

    await db.commit()
    await db.refresh(db_contact)
    return db_contact


async def delete_contact(db: AsyncSession, contact_id: int) -> None:
    """
    Delete a contact by ID. Raises 404 if not found.
    """
    result = await db.execute(
        select(models.Contact).where(models.Contact.id == contact_id)
    )
    db_contact = result.scalar_one_or_none()
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    await db.delete(db_contact)
    await db.commit()

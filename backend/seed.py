import asyncio
from sqlalchemy import select
from src.database.connection import AsyncSessionLocal
from src.contact import models as contact_models
from src.leads import models as lead_models


async def seed():
    async with AsyncSessionLocal() as session:
        # Kontakte prüfen & hinzufügen
        async def get_or_create_contact(first_name, last_name, emails):
            result = await session.execute(
                select(contact_models.Contact).where(
                    contact_models.Contact.first_name == first_name,
                    contact_models.Contact.last_name == last_name,
                )
            )
            contact = result.scalar_one_or_none()
            if not contact:
                contact = contact_models.Contact(
                    first_name=first_name,
                    last_name=last_name,
                    contact_emails=[
                        contact_models.ContactEmail(value=email, is_primary=i == 0)
                        for i, email in enumerate(emails)
                    ],
                )
                session.add(contact)
                await session.flush()
            return contact

        alice = await get_or_create_contact(
            "Alice", "Smith", ["alice@example.com", "alice+work@example.com"]
        )
        bob = await get_or_create_contact("Bob", "Jones", ["bob@example.com"])
        clara = await get_or_create_contact(
            "Clara", "Müller", ["clara@example.com", "clara+sales@example.com"]
        )

        # Leads prüfen & hinzufügen
        async def get_or_create_lead(name, domain, primary_contact):
            result = await session.execute(
                select(lead_models.Lead).where(lead_models.Lead.domain == domain)
            )
            lead = result.scalar_one_or_none()
            if not lead:
                lead = lead_models.Lead(
                    name=name,
                    domain=domain,
                    primary_contact=primary_contact,
                )
                session.add(lead)
            return lead

        await get_or_create_lead("Acme Corp", "acme.com", alice)
        await get_or_create_lead("Beta Ltd", "beta.com", bob)
        await get_or_create_lead("Gamma GmbH", "gamma.de", clara)

        await session.commit()
        print("✅ Seed data inserted (idempotent).")


if __name__ == "__main__":
    asyncio.run(seed())

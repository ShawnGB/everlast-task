from __future__ import annotations
from sqlalchemy import Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from typing import Optional, TYPE_CHECKING
import enum
from src.database.connection import Base

if TYPE_CHECKING:
    from src.contact.models import Contact


class LeadStatus(enum.Enum):
    new = "new"
    qualified = "qualified"
    lost = "lost"


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    domain: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[LeadStatus] = mapped_column(
        Enum(LeadStatus, name="lead_status"),
        default=LeadStatus.new,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    primary_contact_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("contacts.id", ondelete="SET NULL"),
        nullable=True,
    )
    primary_contact: Mapped[Optional["Contact"]] = relationship(back_populates="leads")

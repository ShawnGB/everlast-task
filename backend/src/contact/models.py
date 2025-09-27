from sqlalchemy import Integer, String, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.connection import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)

    contact_emails: Mapped[list["ContactEmail"]] = relationship(
        back_populates="contact", cascade="all, delete-orphan"
    )

    leads = relationship("Lead", back_populates="primary_contact")


class ContactEmail(Base):
    __tablename__ = "contact_emails"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    contact_id: Mapped[int] = mapped_column(
        ForeignKey("contacts.id", ondelete="CASCADE")
    )
    value: Mapped[str] = mapped_column(String(255), nullable=False)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    contact: Mapped["Contact"] = relationship(back_populates="contact_emails")

    __table_args__ = (
        UniqueConstraint("contact_id", "value", name="_contact_id_email_uc"),
    )

"""init schema

Revision ID: 95c95a86276a
Revises:
Create Date: 2025-09-27 16:12:44.089018

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "95c95a86276a"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "contacts",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
    )

    op.create_table(
        "contact_emails",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "contact_id",
            sa.Integer(),
            sa.ForeignKey("contacts.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("value", sa.String(length=255), nullable=False),
        sa.Column("is_primary", sa.Boolean(), nullable=False),
        sa.UniqueConstraint("contact_id", "value", name="_contact_id_email_uc"),
    )
    op.create_index("ix_contact_emails_value", "contact_emails", ["value"])

    op.create_table(
        "leads",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("domain", sa.String(length=255), nullable=False),
        sa.Column(
            "status",
            sa.Enum("new", "qualified", "lost", name="lead_status"),
            nullable=False,
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column(
            "primary_contact_id",
            sa.Integer(),
            sa.ForeignKey("contacts.id", ondelete="SET NULL"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("leads")
    op.drop_index("ix_contact_emails_value", table_name="contact_emails")
    op.drop_table("contact_emails")
    op.drop_table("contacts")

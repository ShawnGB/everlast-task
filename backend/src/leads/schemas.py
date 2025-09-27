from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from src.contact.schemas import ContactCreate


class LeadStatus(str, Enum):
    new = "new"
    qualified = "qualified"
    lost = "lost"


class LeadBase(BaseModel):
    name: str
    domain: str
    status: LeadStatus = LeadStatus.new


class LeadCreate(LeadBase):
    primary_contact_id: Optional[int] = None
    primary_contact: Optional[ContactCreate] = None


class LeadUpdate(BaseModel):
    name: Optional[str] = None
    domain: Optional[str] = None
    status: Optional[LeadStatus] = None
    primary_contact_id: Optional[int] = None


class LeadRead(LeadBase):
    id: int
    created_at: datetime
    primary_contact_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)

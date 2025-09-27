from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict


class ContactEmailBase(BaseModel):
    value: EmailStr
    is_primary: bool = False


class ContactEmailCreate(ContactEmailBase):
    pass


class ContactEmailUpdate(BaseModel):
    value: Optional[EmailStr] = None
    is_primary: Optional[bool] = None


class ContactEmailRead(ContactEmailBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ContactBase(BaseModel):
    first_name: str
    last_name: str


class ContactCreate(ContactBase):
    emails: Optional[List[ContactEmailCreate]] = None


class ContactUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    emails: Optional[List[ContactEmailUpdate]] = None


class ContactRead(ContactBase):
    id: int
    contact_emails: List[ContactEmailRead] = []

    model_config = ConfigDict(from_attributes=True)

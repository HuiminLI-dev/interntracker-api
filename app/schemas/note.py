from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class NoteCreate(BaseModel):
    content: str
    application_id: int


class NoteUpdate(BaseModel):
    content: Optional[str] = None


class NoteOut(BaseModel):
    id: int
    content: str
    application_id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
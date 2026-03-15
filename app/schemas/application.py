from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ApplicationStatus(str, Enum):
    wishlist = "wishlist"
    applied = "applied"
    oa = "oa"
    interview = "interview"
    offer = "offer"
    rejected = "rejected"


class ApplicationCreate(BaseModel):
    role_title: str
    status: ApplicationStatus = ApplicationStatus.wishlist
    source: Optional[str] = None
    job_url: Optional[str] = None
    applied_date: Optional[date] = None
    next_step_date: Optional[date] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    company_id: int


class ApplicationUpdate(BaseModel):
    role_title: Optional[str] = None
    status: Optional[ApplicationStatus] = None
    source: Optional[str] = None
    job_url: Optional[str] = None
    applied_date: Optional[date] = None
    next_step_date: Optional[date] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    company_id: Optional[int] = None


class ApplicationOut(BaseModel):
    id: int
    role_title: str
    status: ApplicationStatus
    source: Optional[str] = None
    job_url: Optional[str] = None
    applied_date: Optional[date] = None
    next_step_date: Optional[date] = None
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    company_id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
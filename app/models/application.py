from datetime import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    role_title = Column(String, index=True, nullable=False)
    status = Column(String, index=True, nullable=False, default="wishlist")
    source = Column(String, nullable=True)
    job_url = Column(String, nullable=True)

    applied_date = Column(Date, nullable=True)
    next_step_date = Column(Date, nullable=True)

    salary_min = Column(Integer, nullable=True)
    salary_max = Column(Integer, nullable=True)

    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    company = relationship("Company", back_populates="applications")
    owner = relationship("User", back_populates="applications")
    notes = relationship("Note", back_populates="application", cascade="all, delete")
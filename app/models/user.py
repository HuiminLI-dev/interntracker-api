from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    companies = relationship("Company", back_populates="owner", cascade="all, delete")
    applications = relationship("Application", back_populates="owner", cascade="all, delete")
    notes = relationship("Note", back_populates="owner", cascade="all, delete")

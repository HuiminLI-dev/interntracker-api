from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.application import Application
from app.models.company import Company
from app.models.user import User
from app.schemas.application import (
    ApplicationCreate,
    ApplicationOut,
    ApplicationUpdate,
)

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("", response_model=ApplicationOut)
def create_application(
    payload: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    company = (
        db.query(Company)
        .filter(Company.id == payload.company_id, Company.owner_id == current_user.id)
        .first()
    )
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    application = Application(**payload.model_dump(), owner_id=current_user.id)
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


@router.get("", response_model=list[ApplicationOut])
def list_applications(
    status: str = "",
    company_id: int = 0,
    search: str = "",
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = db.query(Application).filter(Application.owner_id == current_user.id)

    if status:
        query = query.filter(Application.status == status)

    if company_id:
        query = query.filter(Application.company_id == company_id)

    if search:
        query = query.filter(Application.role_title.ilike(f"%{search}%"))

    applications = (
        query.order_by(Application.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return applications


@router.get("/{application_id}", response_model=ApplicationOut)
def get_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    application = (
        db.query(Application)
        .filter(Application.id == application_id, Application.owner_id == current_user.id)
        .first()
    )
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application


@router.put("/{application_id}", response_model=ApplicationOut)
def update_application(
    application_id: int,
    payload: ApplicationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    application = (
        db.query(Application)
        .filter(Application.id == application_id, Application.owner_id == current_user.id)
        .first()
    )
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    update_data = payload.model_dump(exclude_unset=True)

    if "company_id" in update_data:
        company = (
            db.query(Company)
            .filter(
                Company.id == update_data["company_id"],
                Company.owner_id == current_user.id,
            )
            .first()
        )
        if not company:
            raise HTTPException(status_code=404, detail="Target company not found")

    for key, value in update_data.items():
        setattr(application, key, value)

    db.commit()
    db.refresh(application)
    return application


@router.delete("/{application_id}")
def delete_application(
    application_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    application = (
        db.query(Application)
        .filter(Application.id == application_id, Application.owner_id == current_user.id)
        .first()
    )
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    db.delete(application)
    db.commit()
    return {"message": "Application deleted"}
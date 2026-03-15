from fastapi import FastAPI

from app.api.routes import auth
from app.core.config import settings
from app.core.database import Base, engine
import app.models  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name)


@app.get("/")
def root():
    return {"message": "InternTracker API is running"}


app.include_router(auth.router)
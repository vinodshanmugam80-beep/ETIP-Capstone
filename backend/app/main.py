from fastapi import FastAPI
from app.core.settings import settings
from app.db.init_db import init_db

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {
        "message": "Welcome to ETIP API",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
from fastapi import FastAPI
from app.db.database import engine, Base


app = FastAPI(
    title="IntelForge AI API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "IntelForge AI Backend Running"
    }
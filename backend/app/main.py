from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.business_profile import router as business_profile_router

app = FastAPI(
    title="IntelForge AI",
    version="1.0.0"
)

# Authentication Routes
app.include_router(auth_router)

# Business Profile Routes
app.include_router(business_profile_router)


@app.get("/")
def root():
    return {
        "message": "IntelForge AI API Running"
    }
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.otp_service import create_email_otp

from app.schemas.auth import RegisterRequest
from app.services.user_service import (
    create_user,
    get_user_by_email
)

from app.db.database import get_db
from app.auth.otp import generate_otp


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register_user(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(
        db,
        request.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )


    user = create_user(
        db=db,
        name=request.name,
        email=request.email,
        password=request.password
    )


    otp_record = create_email_otp(
        db=db,
        user_id=user.id
    )


    return {
    "message": "User registered successfully",
    "user_id": user.id,
    "otp_debug": otp_record.otp_code
}
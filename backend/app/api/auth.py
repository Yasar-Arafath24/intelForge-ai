from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.password import verify_password
from app.auth.jwt import create_access_token

from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    VerifyOTPRequest,
)

from app.services.user_service import (
    create_user,
    get_user_by_email
)

from app.services.otp_service import (
    create_email_otp
)

from app.services.otp_verify_service import (
    verify_email_otp
)

from app.services.email_service import (
    send_otp_email
)

from app.db.database import get_db


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ==================================================
# REGISTER USER + SEND OTP
# ==================================================

@router.post("/register")
async def register_user(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    # Check existing email
    existing_user = get_user_by_email(
        db,
        request.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )


    # Create user
    user = create_user(
        db=db,
        name=request.name,
        email=request.email,
        password=request.password
    )


    # Generate OTP
    otp_record = create_email_otp(
        db=db,
        user_id=user.id
    )


    # Send OTP Email
    try:
        await send_otp_email(
            receiver_email=user.email,
            otp_code=otp_record.otp_code
        )

    except Exception as e:
        db.delete(otp_record)
        db.delete(user)
        db.commit()
        raise HTTPException(
            status_code=500,
            detail=f"Email sending failed: {str(e)}"
        )


    return {
        "message": "User registered successfully. OTP sent to email.",
        "user_id": user.id
    }



# ==================================================
# VERIFY EMAIL OTP
# ==================================================

@router.post("/verify-otp")
def verify_otp(
    request: VerifyOTPRequest,
    db: Session = Depends(get_db)
):

    # Find user using email
    user = get_user_by_email(
        db,
        request.email
    )


    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    # Verify OTP
    verified = verify_email_otp(
        db=db,
        user_id=user.id,
        otp_code=request.otp_code
    )


    if not verified:
        raise HTTPException(
            status_code=400,
            detail="Invalid or expired OTP"
        )


    return {
        "message": "Email verified successfully"
    }
    
@router.post("/login", response_model=TokenResponse)
def login_user(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = get_user_by_email(
        db,
        request.email
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        request.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not user.email_verified:
        raise HTTPException(
            status_code=403,
            detail="Email not verified. Please verify your OTP first."
        )

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Account is inactive"
        )

    token = create_access_token({
        "sub": str(user.id),
        "email": user.email
    })

    return TokenResponse(
        access_token=token,
        token_type="bearer"
    )
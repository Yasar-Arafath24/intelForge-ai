from sqlalchemy.orm import Session

from app.models.email_otp import EmailOTP
from app.auth.otp import (
    generate_otp,
    get_otp_expiry
)


def create_email_otp(
    db: Session,
    user_id: str
):

    otp_code = generate_otp()

    otp_record = EmailOTP(
        user_id=user_id,
        otp_code=otp_code,
        expires_at=get_otp_expiry()
    )

    db.add(otp_record)
    db.commit()
    db.refresh(otp_record)

    return otp_record
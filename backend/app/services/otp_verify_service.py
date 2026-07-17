from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.email_otp import EmailOTP
from app.models.user import User


def verify_email_otp(
    db: Session,
    user_id: str,
    otp_code: str
):

    otp_record = (
        db.query(EmailOTP)
        .filter(
            EmailOTP.user_id == user_id,
            EmailOTP.otp_code == otp_code,
            EmailOTP.is_used == False
        )
        .first()
    )


    if not otp_record:
        return False


    current_time = datetime.now(timezone.utc)

    expires_at = otp_record.expires_at
    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=timezone.utc)

    if expires_at < current_time:
        return False


    otp_record.is_used = True


    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


    if user:
        user.email_verified = True


    db.commit()


    return True
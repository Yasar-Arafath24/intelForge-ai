import random
from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.models.email_otp import EmailOTP


def generate_otp():

    return str(random.randint(100000,999999))



def create_email_otp(
    db: Session,
    user_id: str
):

    otp = generate_otp()


    otp_record = EmailOTP(
        user_id=user_id,
        otp_code=otp,
        expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)
    )


    db.add(otp_record)

    db.commit()

    db.refresh(otp_record)


    return otp_record
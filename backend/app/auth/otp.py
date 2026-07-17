import random
from datetime import datetime, timedelta, timezone


def generate_otp() -> str:
    """
    Generate a secure 6 digit OTP
    """

    return str(
        random.randint(
            100000,
            999999
        )
    )


def get_otp_expiry(
    minutes: int = 10
) -> datetime:
    """
    OTP validity period
    """

    return (
        datetime.now(timezone.utc)
        +
        timedelta(minutes=minutes)
    )
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.core.config import settings


conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)


async def send_otp_email(
    receiver_email: str,
    otp_code: str
):

    message = MessageSchema(
        subject="IntelForge AI - Email Verification OTP",
        recipients=[receiver_email],
        body=f"""
Welcome to IntelForge AI.

Your Email Verification OTP is:

{otp_code}

This OTP will expire in 10 minutes.

Do not share this OTP with anyone.
""",
        subtype="plain"
    )


    fm = FastMail(conf)

    await fm.send_message(message)
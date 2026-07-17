from email.message import EmailMessage

import aiosmtplib

from app.core.config import settings



async def send_otp_email(
    receiver_email: str,
    otp_code: str
):

    message = EmailMessage()

    message["From"] = settings.MAIL_FROM

    message["To"] = receiver_email

    message["Subject"] = "IntelForge AI - Email Verification OTP"


    message.set_content(
        f"""
Hello,

Welcome to IntelForge AI.

Your email verification OTP is:

{otp_code}

This OTP is valid for 10 minutes.

If you did not request this, please ignore this email.

Regards,
IntelForge AI Team
"""
    )


    await aiosmtplib.send(
        message,
        hostname=settings.MAIL_SERVER,
        port=settings.MAIL_PORT,
        start_tls=True,
        username=settings.MAIL_USERNAME,
        password=settings.MAIL_PASSWORD
    )
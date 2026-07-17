from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=8
    )


class OTPVerifyRequest(BaseModel):

    email: EmailStr

    otp_code: str = Field(
        min_length=6,
        max_length=6
    )
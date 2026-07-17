from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


ENV_FILE = Path(__file__).resolve().parents[2] / ".env"

load_dotenv(
    ENV_FILE,
    override=False
)


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE),
        env_file_encoding="utf-8",
        extra="ignore",
    )


    # Database
    DATABASE_URL: str = "sqlite:///./app.db"


    # JWT Authentication
    JWT_SECRET_KEY: str = "dev-jwt-secret"

    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

    REFRESH_TOKEN_EXPIRE_DAYS: int = 7


    # Email Configuration
    MAIL_USERNAME: str

    MAIL_PASSWORD: str

    MAIL_FROM: str

    MAIL_PORT: int = 587

    MAIL_SERVER: str = "smtp.gmail.com"



settings = Settings()
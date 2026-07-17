from sqlalchemy import create_engine
from sqlalchemy.exc import ArgumentError
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings


DATABASE_URL = (settings.DATABASE_URL or "sqlite:///./app.db").strip()
ENGINE_KWARGS = {}

if DATABASE_URL.startswith("sqlite"):
    ENGINE_KWARGS["connect_args"] = {"check_same_thread": False}

try:
    engine = create_engine(DATABASE_URL, **ENGINE_KWARGS)
except ArgumentError:
    engine = create_engine("sqlite:///./app.db", connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
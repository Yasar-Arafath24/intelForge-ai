from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class BusinessProfile(Base):
    __tablename__ = "business_profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        String(36),
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    business_name = Column(
        String,
        nullable=False
    )

    industry = Column(
        String,
        nullable=False
    )

    company_size = Column(
        String,
        nullable=False
    )

    website = Column(
        String,
        nullable=True
    )

    country = Column(
        String,
        nullable=False
    )

    city = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="business_profile"
    )
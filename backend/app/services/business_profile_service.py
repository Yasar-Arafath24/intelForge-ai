from sqlalchemy.orm import Session

from app.models.business_profile import BusinessProfile


def create_business_profile(
    db: Session,
    user_id: str,
    business_name: str,
    industry: str,
    company_size: str,
    website: str | None,
    country: str,
    city: str,
    description: str,
):
    profile = BusinessProfile(
        user_id=user_id,
        business_name=business_name,
        industry=industry,
        company_size=company_size,
        website=website,
        country=country,
        city=city,
        description=description,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def get_business_profile(
    db: Session,
    user_id: str,
):
    return (
        db.query(BusinessProfile)
        .filter(BusinessProfile.user_id == user_id)
        .first()
    )


def update_business_profile(
    db: Session,
    profile: BusinessProfile,
    data: dict,
):
    for key, value in data.items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)

    return profile
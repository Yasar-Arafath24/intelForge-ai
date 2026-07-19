from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.business_profile import (
    BusinessProfileCreate,
    BusinessProfileResponse
)

from app.services.business_profile_service import (
    create_business_profile,
    get_business_profile
)

from app.auth.dependencies import get_current_user


router = APIRouter(
    prefix="/business-profile",
    tags=["Business Profile"]
)


@router.post(
    "/",
    response_model=BusinessProfileResponse
)
def create_profile(
    request: BusinessProfileCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    existing_profile = get_business_profile(
        db,
        current_user.id
    )

    if existing_profile:
        raise HTTPException(
            status_code=400,
            detail="Business profile already exists"
        )

    profile = create_business_profile(
        db=db,
        user_id=current_user.id,
        business_name=request.business_name,
        industry=request.industry,
        company_size=request.company_size,
        website=str(request.website) if request.website else None,
        country=request.country,
        city=request.city,
        description=request.description
    )

    return profile


@router.get(
    "/me",
    response_model=BusinessProfileResponse
)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    profile = get_business_profile(
        db,
        current_user.id
    )

    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Business profile not found"
        )

    return profile
from pydantic import BaseModel, HttpUrl
from typing import Optional


class BusinessProfileCreate(BaseModel):
    business_name: str
    industry: str
    company_size: str
    website: Optional[HttpUrl] = None
    country: str
    city: str
    description: str


class BusinessProfileResponse(BaseModel):
    id: int
    business_name: str
    industry: str
    company_size: str
    website: Optional[str] = None
    country: str
    city: str
    description: str

    model_config = {
        "from_attributes": True
    }
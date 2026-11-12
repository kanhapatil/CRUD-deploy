from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# Request schema: Create user
class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr


# Request schema: Update user
class UserUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr


# Response schema: User details
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
"""User model for the Recipamatic API."""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserRole(str, Enum):
    """User roles for the Recipamatic API."""

    ADMIN = "admin"
    USER = "user"


class UserBase(BaseModel):
    """Base user model."""

    email: EmailStr
    name: str
    picture: Optional[str] = None


class UserCreate(UserBase):
    """User creation model."""

    pass


class User(UserBase):
    """User model."""

    id: str
    role: UserRole = UserRole.USER
    created_at: datetime = Field(default_factory=datetime.now)
    last_login: Optional[datetime] = None

    class Config:
        """Config for the User model."""

        json_schema_extra = {
            "example": {
                "id": "google-oauth2|123456789",
                "email": "user@example.com",
                "name": "Test User",
                "picture": "https://example.com/avatar.jpg",
                "role": "user",
                "created_at": "2025-04-13T12:00:00",
                "last_login": "2025-04-13T12:00:00",
            }
        }

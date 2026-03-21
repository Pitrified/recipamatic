"""Authentication settings for the Recipamatic API."""

import os
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class AuthSettings(BaseSettings):
    """Authentication settings for the Recipamatic API."""

    # JWT settings
    SECRET_KEY: str = Field(
        default="your-secret-key-for-development-only-change-in-production",
        env="RECIPAMATIC_SECRET_KEY",
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 * 24 * 60  # 30 days

    # Google OAuth settings
    GOOGLE_CLIENT_ID: Optional[str] = Field(None, env="RECIPAMATIC_GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: Optional[str] = Field(
        None, env="RECIPAMATIC_GOOGLE_CLIENT_SECRET"
    )
    GOOGLE_REDIRECT_URI: str = Field(
        "http://localhost:5173/auth/callback", env="RECIPAMATIC_GOOGLE_REDIRECT_URI"
    )

    # Frontend settings
    FRONTEND_URL: str = Field("http://localhost:5173", env="RECIPAMATIC_FRONTEND_URL")
    AUTH_REDIRECT_PATH: str = "/auth/callback"
    LOGIN_SUCCESS_REDIRECT: str = "/recipes"
    LOGIN_FAILURE_REDIRECT: str = "/login?error=auth_failed"

    class Config:
        """Configuration for AuthSettings."""

        # Only use env_file if it exists
        env_file = (
            "/home/pmn/cred/recipamatic/.env"
            if os.path.exists("/home/pmn/cred/recipamatic/.env")
            else None
        )
        env_file_encoding = "utf-8"
        # Extra settings to make development easier
        validate_assignment = True
        extra = "ignore"
        arbitrary_types_allowed = True


# Create a singleton instance
auth_settings = AuthSettings()

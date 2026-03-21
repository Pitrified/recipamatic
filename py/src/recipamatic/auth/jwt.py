"""JWT token handling for the Recipamatic API."""

from datetime import datetime, timedelta
from typing import Dict, Optional

from jose import JWTError, jwt
from pydantic import BaseModel
from recipamatic.auth.settings import auth_settings


class TokenData(BaseModel):
    """Token data model."""

    sub: str
    exp: datetime


def create_access_token(
    data: Dict[str, str], expires_delta: Optional[timedelta] = None
) -> str:
    """Create a JWT access token."""
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=auth_settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, auth_settings.SECRET_KEY, algorithm=auth_settings.ALGORITHM
    )
    return encoded_jwt


def decode_access_token(token: str) -> Optional[TokenData]:
    """Decode a JWT access token."""
    try:
        payload = jwt.decode(
            token, auth_settings.SECRET_KEY, algorithms=[auth_settings.ALGORITHM]
        )
        user_id: str = payload.get("sub")
        expiration: datetime = datetime.fromtimestamp(payload.get("exp"))

        if user_id is None:
            return None

        return TokenData(sub=user_id, exp=expiration)
    except JWTError:
        return None

"""Authentication dependencies for the Recipamatic API."""

from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from recipamatic.auth.jwt import decode_access_token
from recipamatic.auth.models import User
from recipamatic.auth.repository import user_repository

# OAuth2 scheme for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/token",
    scheme_name="JWT",
    auto_error=False,
)


async def get_current_user(
    token: Optional[str] = Depends(oauth2_scheme),
) -> Optional[User]:
    """Get the current user from a JWT token.

    If no token or invalid token, returns None.
    """
    if not token:
        return None

    token_data = decode_access_token(token)
    if token_data is None:
        return None

    user = user_repository.get_user(token_data.sub)
    return user


async def get_current_active_user(
    current_user: Optional[User] = Depends(get_current_user),
) -> User:
    """Get the current active user, raising an exception if not authenticated."""
    if current_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return current_user

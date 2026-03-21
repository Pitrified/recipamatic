"""Authentication router for the Recipamatic API."""

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from loguru import logger as lg
from recipamatic.auth.dependencies import get_current_active_user
from recipamatic.auth.jwt import create_access_token
from recipamatic.auth.models import User
from recipamatic.auth.oauth import google_oauth
from recipamatic.auth.settings import auth_settings

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/login/google")
async def login_google():
    """Redirect to Google login."""
    try:
        authorize_url = google_oauth.get_authorization_url()
        return RedirectResponse(authorize_url)
    except ValueError as e:
        lg.error(f"Error getting Google authorization URL: {e}")
        return RedirectResponse(
            url=f"{auth_settings.FRONTEND_URL}{auth_settings.LOGIN_FAILURE_REDIRECT}&error=oauth_config"
        )


@router.get("/callback")
async def auth_callback(code: str = None, error: str = None):
    """Handle the OAuth callback."""
    # Handle error from OAuth provider
    if error:
        lg.error(f"OAuth error received: {error}")
        return RedirectResponse(
            url=f"{auth_settings.FRONTEND_URL}{auth_settings.LOGIN_FAILURE_REDIRECT}&error={error}"
        )

    # Ensure code is provided
    if not code:
        lg.error("No authorization code received in callback")
        return RedirectResponse(
            url=f"{auth_settings.FRONTEND_URL}{auth_settings.LOGIN_FAILURE_REDIRECT}&error=no_code"
        )

    try:
        # Authenticate user with Google
        user = google_oauth.authenticate(code)
        if not user:
            lg.error("Failed to authenticate user with Google")
            return RedirectResponse(
                url=f"{auth_settings.FRONTEND_URL}{auth_settings.LOGIN_FAILURE_REDIRECT}&error=auth_failed"
            )

        # Create access token
        access_token = create_access_token(data={"sub": user.id})

        # Redirect to frontend with token
        redirect_url = f"{auth_settings.FRONTEND_URL}{auth_settings.LOGIN_SUCCESS_REDIRECT}?token={access_token}"
        return RedirectResponse(url=redirect_url)
    except Exception as e:
        lg.error(f"Error in auth callback: {e}")
        return RedirectResponse(
            url=f"{auth_settings.FRONTEND_URL}{auth_settings.LOGIN_FAILURE_REDIRECT}&error=server_error"
        )


@router.get("/me", response_model=User)
async def get_current_user(current_user: User = Depends(get_current_active_user)):
    """Get the current user."""
    return current_user


@router.post("/logout")
async def logout():
    """Logout the user.

    Note: This is handled on the client side by removing the token.
    This endpoint is just for API completeness.
    """
    return {"message": "Logged out successfully"}

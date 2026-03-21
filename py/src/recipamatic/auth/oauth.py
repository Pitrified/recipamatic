"""OAuth providers for Recipamatic API."""

import json
from typing import Dict, Optional

from authlib.integrations.requests_client import OAuth2Session
from loguru import logger as lg
from recipamatic.auth.models import User, UserCreate
from recipamatic.auth.repository import user_repository
from recipamatic.auth.settings import auth_settings


class GoogleOAuth:
    """Google OAuth provider."""

    def __init__(self):
        """Initialize the Google OAuth provider."""
        self.client_id = auth_settings.GOOGLE_CLIENT_ID
        self.client_secret = auth_settings.GOOGLE_CLIENT_SECRET
        self.redirect_uri = auth_settings.GOOGLE_REDIRECT_URI
        self.scope = "openid email profile"
        self.auth_endpoint = "https://accounts.google.com/o/oauth2/auth"
        self.token_endpoint = "https://oauth2.googleapis.com/token"
        self.user_info_endpoint = "https://www.googleapis.com/oauth2/v1/userinfo"

        # Log initialization state
        if not self.client_id or not self.client_secret:
            lg.warning(
                "Google OAuth credentials not configured. Authentication features will be limited."
            )
        else:
            lg.info("Google OAuth configured successfully.")

    def get_authorization_url(self) -> str:
        """Get the Google authorization URL."""
        if not self.client_id or not self.client_secret:
            lg.error("Google OAuth client ID or secret not configured")
            raise ValueError("Google OAuth not properly configured")

        try:
            client = OAuth2Session(
                client_id=self.client_id,
                client_secret=self.client_secret,
                scope=self.scope,
            )

            url, state = client.create_authorization_url(
                self.auth_endpoint,
                redirect_uri=self.redirect_uri,
                access_type="offline",
                prompt="consent",
            )

            lg.debug(f"Generated Google authorization URL with state: {state}")
            return url
        except Exception as e:
            lg.error(f"Error generating authorization URL: {e}")
            raise ValueError(f"Failed to generate authorization URL: {str(e)}")

    def get_user_info(self, code: str) -> Optional[Dict]:
        """Get user info from the authorization code."""
        if not self.client_id or not self.client_secret:
            lg.error("Google OAuth client ID or secret not configured")
            return None

        try:
            client = OAuth2Session(
                client_id=self.client_id,
                client_secret=self.client_secret,
                scope=self.scope,
            )

            # Exchange the authorization code for an access token
            token_response = client.fetch_token(
                self.token_endpoint,
                authorization_response=f"{self.redirect_uri}?code={code}",
                redirect_uri=self.redirect_uri,
            )

            # Use the access token to get user info
            resp = client.get(self.user_info_endpoint)
            if resp.status_code == 200:
                user_info = resp.json()
                lg.debug(f"Retrieved user info: {json.dumps(user_info, indent=2)}")
                return user_info
            else:
                lg.error(f"Failed to get user info: {resp.status_code} {resp.text}")
                return None
        except Exception as e:
            lg.error(f"Error getting user info: {e}")
            return None

    def authenticate(self, code: str) -> Optional[User]:
        """Authenticate a user with Google OAuth."""
        user_info = self.get_user_info(code)
        if not user_info:
            return None

        # Check if user exists
        user_id = f"google-oauth2|{user_info.get('id')}"
        user = user_repository.get_user(user_id)

        if user:
            # Update user info and last login time
            user.name = user_info.get("name", user.name)
            user.picture = user_info.get("picture", user.picture)
            user = user_repository.update_last_login(user.id)
            return user
        else:
            # Create new user
            user_data = UserCreate(
                email=user_info.get("email"),
                name=user_info.get("name", ""),
                picture=user_info.get("picture"),
            )
            return user_repository.create_user(user_data, user_id)


# Create a singleton instance
google_oauth = GoogleOAuth()

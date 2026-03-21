"""User repository for the Recipamatic API."""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional

from loguru import logger as lg
from recipamatic.auth.models import User, UserCreate
from recipamatic.config.recipamatic_config import RecipamaticConfig


class UserRepository:
    """Repository for user management."""

    def __init__(self):
        """Initialize the user repository."""
        try:
            self.config = RecipamaticConfig()
            # Use data_fol instead of data_dir which doesn't exist
            self.users_dir = os.path.join(self.config.paths.data_fol, "users")
            os.makedirs(self.users_dir, exist_ok=True)
            self._users: Dict[str, User] = {}
            self._load_users()
            lg.info(f"User repository initialized at {self.users_dir}")
        except Exception as e:
            lg.error(f"Error initializing user repository: {e}")
            # Fallback to a default directory if data_fol is not available
            self.users_dir = os.path.join(
                os.path.expanduser("~"), ".recipamatic", "users"
            )
            os.makedirs(self.users_dir, exist_ok=True)
            self._users: Dict[str, User] = {}
            lg.warning(f"Using fallback user directory: {self.users_dir}")

    def _load_users(self) -> None:
        """Load users from the filesystem."""
        try:
            if not os.path.exists(self.users_dir):
                lg.warning(f"Users directory does not exist: {self.users_dir}")
                return

            for filename in os.listdir(self.users_dir):
                if filename.endswith(".json"):
                    try:
                        with open(os.path.join(self.users_dir, filename), "r") as f:
                            user_data = json.load(f)
                            # Convert string timestamps to datetime objects
                            if "created_at" in user_data and user_data["created_at"]:
                                user_data["created_at"] = datetime.fromisoformat(
                                    user_data["created_at"]
                                )
                            if "last_login" in user_data and user_data["last_login"]:
                                user_data["last_login"] = datetime.fromisoformat(
                                    user_data["last_login"]
                                )
                            user = User(**user_data)
                            self._users[user.id] = user
                    except Exception as e:
                        lg.error(f"Error loading user from {filename}: {e}")
        except Exception as e:
            lg.error(f"Error loading users from directory: {e}")

    def _save_user(self, user: User) -> None:
        """Save a user to the filesystem."""
        try:
            if not os.path.exists(self.users_dir):
                os.makedirs(self.users_dir, exist_ok=True)

            user_filename = os.path.join(self.users_dir, f"{user.id}.json")
            user_dict = user.model_dump()
            # Convert datetime objects to ISO format strings for JSON serialization
            if user_dict["created_at"]:
                user_dict["created_at"] = user_dict["created_at"].isoformat()
            if user_dict["last_login"]:
                user_dict["last_login"] = user_dict["last_login"].isoformat()

            with open(user_filename, "w") as f:
                json.dump(user_dict, f, indent=2)
        except Exception as e:
            lg.error(f"Error saving user {user.id}: {e}")

    def get_user(self, user_id: str) -> Optional[User]:
        """Get a user by ID."""
        return self._users.get(user_id)

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Get a user by email."""
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def create_user(self, user_data: UserCreate, user_id: str) -> User:
        """Create a new user."""
        user = User(id=user_id, **user_data.model_dump())
        self._users[user.id] = user
        self._save_user(user)
        return user

    def update_user(self, user: User) -> User:
        """Update a user."""
        self._users[user.id] = user
        self._save_user(user)
        return user

    def update_last_login(self, user_id: str) -> Optional[User]:
        """Update the last login time for a user."""
        user = self.get_user(user_id)
        if user:
            user.last_login = datetime.now()
            self._save_user(user)
        return user

    def get_all_users(self) -> List[User]:
        """Get all users."""
        return list(self._users.values())


# Create a singleton instance
try:
    user_repository = UserRepository()
except Exception as e:
    lg.error(f"Error creating user repository: {e}")

    # Create a dummy repository that doesn't require filesystem access
    class DummyUserRepository:
        def get_user(self, user_id):
            return None

        def get_user_by_email(self, email):
            return None

        def create_user(self, user_data, user_id):
            return None

        def update_user(self, user):
            return None

        def update_last_login(self, user_id):
            return None

        def get_all_users(self):
            return []

    user_repository = DummyUserRepository()
    lg.warning("Using dummy user repository due to initialization error")

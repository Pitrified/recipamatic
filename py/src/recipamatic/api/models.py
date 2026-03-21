"""Data model for request/response FastAPI objects."""

from enum import StrEnum
from typing import Optional

from pydantic import BaseModel, Field


class RecipeSource(StrEnum):
    """Possible recipe sources."""

    IG = "ig"
    NOTE = "note"
    MANUAL = "manual"


class RecipeInfoMini(BaseModel):
    """Minimal class for recipe information."""

    name: str = Field(..., description="The name of the recipe.")
    source: RecipeSource = Field(..., description="The source of the recipe.")
    code: str = Field(..., description="The code of the recipe.")
    user_id: Optional[str] = Field(
        None, description="The ID of the user who owns this recipe."
    )
    is_public: bool = Field(
        True, description="Whether this recipe is public or private."
    )


class AudioFile(BaseModel):
    filename: str = Field(..., description="The name of the audio file.")
    content_type: str = Field(..., description="The content type of the audio file.")
    size: int = Field(..., description="The size of the audio file.")
    content: bytes = Field(..., description="The content of the audio file.")

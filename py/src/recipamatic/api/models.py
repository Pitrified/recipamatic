"""Data model for request/response FastAPI objects."""

from enum import Enum, StrEnum

from pydantic import BaseModel, Field


class RecipeSource(StrEnum):
    """Possible recipe sources."""

    IG = "ig"
    MANUAL = "manual"


class RecipeInfoMini(BaseModel):
    """Minimal class for recipe information."""

    name: str = Field(..., description="The name of the recipe.")
    source: RecipeSource = Field(..., description="The source of the recipe.")
    code: str = Field(..., description="The code of the recipe.")

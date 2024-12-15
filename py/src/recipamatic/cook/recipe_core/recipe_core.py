"""Recipe core is the main recipe: ingredients, instructions and notes."""

from enum import Enum

from pydantic import BaseModel, Field


class Ingredient(BaseModel):
    """Represents a single ingredient."""

    name: str = Field(..., description="The name of the ingredient.")
    quantity: str = Field(
        ...,
        description="The quantity of the ingredient. Includes both the amount and the unit.",
    )


class StepType(str, Enum):
    """Enumeration of possible step types."""

    TEXT = "text"
    # IMAGE = "image"


class Step(BaseModel):
    """Represents a preparation step."""

    type: StepType = Field(
        ..., description="The type of step (e.g., 'text' or 'image')."
    )
    instruction: str | None = Field(
        None, description="The explanation for this step, if text."
    )
    # filename: str | None = Field( None, description="The filename of the image, if an image step.")
    # alttext: str | None = Field( None, description="A short description of the image content, for accessibility.")


class Preparation(BaseModel):
    """Represents a preparation section with ingredients and steps."""

    preparation_name: str | None = Field(
        None,
        description="The name of the preparation section. Can be None for the main preparation.",
    )
    ingredients: list[Ingredient] = Field(
        ..., description="A list of ingredients for this preparation."
    )
    steps: list[Step] = Field(..., description="A list of steps for this preparation.")


class RecipeCore(BaseModel):
    """Represents the core of a recipe.

    A recipe consists of several preparation sections, each with ingredients and steps.
    """

    preparations: list[Preparation] = Field(
        ...,
        description="A list of preparation sections, each with ingredients and steps.",
    )
    notes: list[str] | None = Field(None, description="Optional notes for the recipe.")

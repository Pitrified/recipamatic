"""Identify the index of the step and preparation in a RecipeCore object."""

from enum import Enum

from pydantic import BaseModel, Field


class SectionPreparation(BaseModel):
    """Represents a section of a recipe.

    A recipe has several preparations.
    Each preparation has ingredients and steps.
    """

    preparation_idx: int = Field(
        ...,
        description="The index of the preparation in the recipe preparations list.",
    )


class SectionIngredient(SectionPreparation):
    """Represents an ingredient in a section."""

    ingredient_idx: int = Field(
        ...,
        description="The index of the ingredient in the preparation ingredients list.",
    )


class SectionStep(SectionPreparation):
    """Represents a step in a section."""

    step_idx: int = Field(
        ...,
        description="The index of the step in the preparation steps list.",
    )


SectionGen = SectionStep | SectionIngredient


class Section(BaseModel):
    """Represents a section in a RecipeCore object.

    Note that all indexes are 1-based.
    Match the numbers said in the user instruction.
    """

    section: SectionGen = Field(
        ...,
        description="The section in the RecipeCore object.",
    )

"""Take notes while cooking a recipe."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Note(BaseModel):
    """Represents a note for a recipe."""

    text: str = Field(
        ...,
        description="The text of the note.",
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="The timestamp when the note was taken.",
    )


class RecipeNote(BaseModel):
    """Represents a note for a recipe."""

    start_timestamp: datetime = Field(
        default_factory=datetime.now,
        description="The timestamp when the note was taken.",
    )
    notes: list[Note] = Field(
        default_factory=list,
        description="A list of notes for the recipe.",
    )

    def add_note(self, text: str) -> None:
        """Add a note to the recipe."""
        note = Note(
            text=text,
        )
        self.notes.append(note)

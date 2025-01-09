"""Take notes while cooking a recipe."""

from datetime import datetime, timedelta
from enum import Enum

from pydantic import BaseModel, Field

from recipamatic.utils.datetime_ import format_time_delta


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

    def to_string(self) -> str:
        """Return a string representation of the recipe note.

        Clean up the times before returning the string.
        """
        cns = []
        for note in self.notes:
            delta = note.timestamp - self.start_timestamp
            # format the time as minutes and seconds
            delta_f = format_time_delta(delta)
            cn = f"{delta_f}: {note.text}"
            cns.append(cn)
        return "\n".join(cns)

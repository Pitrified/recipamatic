"""A holder for a recipe note.

If the requested note is not found, create an empty one.
The file name is note_date_time.json.
"""

from datetime import datetime
from pathlib import Path

from loguru import logger as lg

from recipamatic.config.recipamatic_config import get_recipamatic_paths
from recipamatic.cook.recipe_note.model import RecipeNote
from recipamatic.utils.datetime_ import FMT_DATETIME
from recipamatic.utils.pathlib_ import check_create_fol


class RecipeNoteHolder:
    """A holder for a recipe note."""

    def __init__(
        self,
        note_code: str | None = None,
    ) -> None:
        """Create a holder for a recipe note."""
        self.notes_fol = get_recipamatic_paths().notes_fol

        self.note_code = note_code
        if note_code is not None:
            self.load_note()
        else:
            self.create_note()

    def generate_note_code(self) -> None:
        """Get the note code for the timestamp."""
        self.timestamp: datetime = datetime.now()
        self.note_code = self.timestamp.strftime(FMT_DATETIME)

    def build_note_fp(self) -> Path:
        """Build the file path for the note."""
        return self.notes_fol / f"note_{self.note_code}.json"

    def load_note(self) -> None:
        """Load the note from the file."""
        note_fp = self.build_note_fp()

        # if the file is not found, create a new note
        if not note_fp.exists():
            lg.warning(f"Note not found: {note_fp}, creating it")
            self.create_note()
            return

        # load the note from the file
        self.note = RecipeNote.model_validate_json(note_fp.read_text())
        self.timestamp = self.note.start_timestamp

    def create_note(self) -> None:
        """Create a new note."""
        self.generate_note_code()
        self.note = RecipeNote(start_timestamp=self.timestamp)
        self.save_note()

    def save_note(self) -> None:
        """Save the note to the file."""
        note_fp = self.build_note_fp()
        check_create_fol(note_fp.parent)
        note_fp.write_text(self.note.model_dump_json(indent=4))

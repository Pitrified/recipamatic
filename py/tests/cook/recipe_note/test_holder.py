import pytest

from recipamatic.cook.recipe_note.holder import RecipeNoteHolder


def test_new_note_creation():
    """Test creating a new note."""
    rh1 = RecipeNoteHolder.new_note()
    assert rh1.note_code is not None
    assert rh1.note is not None


def test_load_existing_note():
    """Test loading an existing note."""
    rh1 = RecipeNoteHolder.new_note()
    note_code = rh1.note_code
    rh2 = RecipeNoteHolder.from_note_code(note_code=note_code)
    assert rh2.note_code == note_code
    assert rh2.note is not None


def test_load_non_existent_note():
    """Test loading a non-existent note code."""
    with pytest.raises(FileNotFoundError):
        RecipeNoteHolder.from_note_code(note_code="not_existent")

"""CRUD operations.

We do not have a real database so we just read a local JSON file.
"""

from typing import Optional

from loguru import logger as lg
from recipamatic.api.models import RecipeInfoMini, RecipeSource
from recipamatic.config.recipamatic_config import get_recipamatic_paths
from recipamatic.cook.recipe_core.recipe_core import RecipeCore
from recipamatic.cook.recipe_note.holder import RecipeNoteHolder
from recipamatic.cook.recipe_note.model import RecipeNote


def load_recipe_list(user_id: Optional[str] = None) -> list[RecipeInfoMini]:
    """Get the list of recipes.

    Args:
        user_id: Optional user ID to filter recipes by ownership.
               If provided, returns public recipes and the user's private recipes.
               If None, returns only public recipes.
    """
    recipes_fol = get_recipamatic_paths().recipes_fol

    recipe_list = []
    for recipe_fol in recipes_fol.iterdir():
        code = recipe_fol.name
        rc_fp = recipe_fol / "recipe_core.json"
        if not rc_fp.exists():
            lg.warning(f"Recipe file not found: {rc_fp}")
            continue

        try:
            rc = RecipeCore.model_validate_json(rc_fp.read_text())

            # Handle recipes without user_id or is_public fields (legacy recipes)
            if not hasattr(rc, "user_id"):
                rc.user_id = None
            if not hasattr(rc, "is_public"):
                rc.is_public = True
            if not hasattr(rc, "source"):
                rc.source = "Instagram"

            # Filter by user_id if provided
            if rc.user_id and not rc.is_public and rc.user_id != user_id:
                # Skip private recipes that don't belong to the current user
                continue

            # Determine source type
            source_type = RecipeSource.IG
            if rc.source == "Voice Note":
                source_type = RecipeSource.NOTE
            elif rc.source == "Manual Entry":
                source_type = RecipeSource.MANUAL

            # Create recipe info with safe defaults
            try:
                recipe_info = RecipeInfoMini(
                    name=rc.name,
                    source=source_type,
                    code=code,
                    user_id=rc.user_id,
                    is_public=rc.is_public,
                )
            except Exception as e:
                # Handle case where fields may be missing
                lg.error(f"Error creating RecipeInfoMini for {code}: {e}")
                recipe_info = RecipeInfoMini(
                    name=rc.name,
                    source=RecipeSource.IG,
                    code=code,
                    user_id=None,
                    is_public=True,
                )

            recipe_list.append(recipe_info)
        except Exception as e:
            lg.error(f"Error loading recipe {code}: {e}")

    return recipe_list


def load_recipe(code: str) -> RecipeCore | None:
    """Get a recipe by code."""
    recipes_fol = get_recipamatic_paths().recipes_fol
    recipe_fol = recipes_fol / code
    if not recipe_fol.exists():
        return None

    rc_fp = recipe_fol / "recipe_core.json"
    if not rc_fp.exists():
        return None

    try:
        rc = RecipeCore.model_validate_json(rc_fp.read_text())

        # Handle recipes without user_id or is_public fields (legacy recipes)
        if not hasattr(rc, "user_id"):
            rc.user_id = None
        if not hasattr(rc, "is_public"):
            rc.is_public = True
        if not hasattr(rc, "source"):
            rc.source = "Instagram"

        return rc
    except Exception as e:
        lg.error(f"Error loading recipe {code}: {e}")
        return None


def create_recipe_note(user_id: Optional[str] = None) -> str:
    """Create a new recipe note.

    Args:
        user_id: Optional user ID to associate with the note.
    """
    rnh = RecipeNoteHolder.new_note()

    # Add user_id to the note if provided
    if user_id:
        rnh.note.user_id = user_id
        rnh.save_note()

    return rnh.note_code


def load_recipe_note(code: str) -> RecipeNote | None:
    """Get a recipe note by code."""
    rnh = load_recipe_note_holder(code=code)
    if rnh is None:
        return None

    # Ensure user_id exists, even if None
    if not hasattr(rnh.note, "user_id"):
        rnh.note.user_id = None

    return rnh.note


def load_recipe_note_holder(code: str) -> RecipeNoteHolder | None:
    """Get a recipe note holder by code."""
    try:
        rnh = RecipeNoteHolder.from_note_code(note_code=code)
        return rnh
    except FileNotFoundError:
        # if the note is not found, return None
        return None

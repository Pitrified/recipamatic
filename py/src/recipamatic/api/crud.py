"""CRUD operations.

We do not have a real database so we just read a local JSON file.
"""

from recipamatic.api.models import RecipeInfoMini, RecipeSource
from recipamatic.config.recipamatic_config import get_recipamatic_paths
from recipamatic.cook.recipe_core.recipe_core import RecipeCore


def load_recipe_list() -> list[RecipeInfoMini]:
    """Get the list of recipes."""
    recipes_fol = get_recipamatic_paths().recipes_fol

    recipe_list = []
    for recipe_fol in recipes_fol.iterdir():
        code = recipe_fol.name
        rc_fp = recipe_fol / f"recipe_core.json"
        rc = RecipeCore.model_validate_json(rc_fp.read_text())
        recipe_info = RecipeInfoMini(
            name=rc.name,
            source=RecipeSource.IG,
            code=code,
        )
        recipe_list.append(recipe_info)

    return recipe_list


def load_recipe(code: str) -> RecipeCore | None:
    """Get a recipe by code."""
    recipes_fol = get_recipamatic_paths().recipes_fol
    recipe_fol = recipes_fol / code
    if not recipe_fol.exists():
        return None

    rc_fp = recipe_fol / f"recipe_core.json"
    rc = RecipeCore.model_validate_json(rc_fp.read_text())
    return rc

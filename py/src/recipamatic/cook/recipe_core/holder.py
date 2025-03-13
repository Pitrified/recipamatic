"""A holder for a recipe core.

If the requested recipe is not found, create an empty one.
The file name is recipe_code/recipe_core.json.
"""

from pathlib import Path
from typing import Self

from recipamatic.config.recipamatic_config import get_recipamatic_paths
from recipamatic.cook.recipe_core.recipe_core import RecipeCore
from recipamatic.utils.pathlib_ import check_create_fol


class RecipeCoreHolder:
    """A holder for a recipe core."""

    def __init__(
        self,
        recipe_code: str,
    ) -> None:
        """Create a holder for a recipe core."""
        self.recipes_fol = get_recipamatic_paths().recipes_fol
        self.recipe_code = recipe_code

    @classmethod
    def from_recipe_code(cls, recipe_code: str) -> Self:
        """Create a holder from a recipe code."""
        recipe = cls(recipe_code=recipe_code)
        recipe.load_recipe()
        return recipe

    @classmethod
    def from_recipe(cls, recipe_code: str, recipe: RecipeCore) -> Self:
        """Create a holder from a RecipeCore object."""
        holder = cls(recipe_code=recipe_code)
        holder.recipe = recipe
        return holder

    @classmethod
    def new_recipe(cls, recipe_code: str) -> Self:
        """Create a holder for a new recipe with the given code."""
        recipe = cls(recipe_code=recipe_code)
        recipe.create_recipe()
        return recipe

    def build_recipe_fp(self) -> Path:
        """Build the file path for the recipe."""
        return self.recipes_fol / self.recipe_code / "recipe_core.json"

    def load_recipe(self) -> None:
        """Load the recipe from the file."""
        recipe_fp = self.build_recipe_fp()

        # if the file is not found, fails
        if not recipe_fp.exists():
            raise FileNotFoundError(f"Recipe not found: {recipe_fp}")

        # load the recipe from the file
        self.recipe = RecipeCore.model_validate_json(recipe_fp.read_text())

    def create_recipe(self) -> None:
        """Create a new recipe."""
        self.recipe = RecipeCore(
            name=self.recipe_code,
            preparations=[],
            notes=[],
        )
        self.save_recipe()

    def save_recipe(self) -> None:
        """Save the recipe to the file."""
        recipe_fp = self.build_recipe_fp()
        check_create_fol(recipe_fp.parent)
        recipe_fp.write_text(self.recipe.model_dump_json(indent=4))

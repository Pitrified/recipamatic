"""FastAPI backend for the Recipamatic API."""

from fastapi import FastAPI

from recipamatic.api.models import RecipeInfoMini, RecipeSource

app = FastAPI()

# Sample data
recipes: list[RecipeInfoMini] = [
    RecipeInfoMini(
        name="Spaghetti Carbonara", source=RecipeSource.MANUAL, code="SC123"
    ),
    RecipeInfoMini(name="Instagram Salad", source=RecipeSource.IG, code="IS456"),
]


@app.get("/recipe_list", response_model=list[RecipeInfoMini])
async def get_recipe_list() -> list[RecipeInfoMini]:
    """Endpoint to get the list of recipes."""
    return recipes

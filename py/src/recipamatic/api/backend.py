"""FastAPI backend for the Recipamatic API."""

from fastapi import FastAPI

from recipamatic.api.crud import recipe_list
from recipamatic.api.models import RecipeInfoMini, RecipeSource

app = FastAPI()


@app.get("/recipe_list", response_model=list[RecipeInfoMini])
async def get_recipe_list() -> list[RecipeInfoMini]:
    """Endpoint to get the list of recipes."""
    return recipe_list()

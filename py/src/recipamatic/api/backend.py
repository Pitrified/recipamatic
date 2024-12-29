"""FastAPI backend for the Recipamatic API."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from recipamatic.api.crud import load_recipe, load_recipe_list
from recipamatic.api.models import RecipeInfoMini, RecipeSource
from recipamatic.cook.recipe_core.recipe_core import RecipeCore

app = FastAPI()


# define allowed origins (replace with your frontend's URL in production)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/recipe_list", response_model=list[RecipeInfoMini])
async def get_recipe_list() -> list[RecipeInfoMini]:
    """Endpoint to get the list of recipes."""
    return load_recipe_list()


@app.get("/recipes/{code}/show", response_model=RecipeCore)
async def show_recipe(code: str) -> RecipeCore:
    """Endpoint to get a specific recipe by code."""
    recipe = load_recipe(code)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

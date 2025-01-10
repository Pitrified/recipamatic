"""FastAPI backend for the Recipamatic API."""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger as lg

from recipamatic.api.crud import create_recipe_note, load_recipe, load_recipe_list
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
    lg.debug(f"get_recipe_list")
    return load_recipe_list()


@app.get("/recipes/{code}/show", response_model=RecipeCore)
async def show_recipe(code: str) -> RecipeCore:
    """Endpoint to get a specific recipe by code."""
    lg.debug(f"show_recipe: code={code}")
    recipe = load_recipe(code)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@app.post("/recipe_note_create", response_model=str)
async def create_note() -> str:
    """Endpoint to create a new recipe note."""
    lg.debug(f"create_note")
    note_code = create_recipe_note()
    return note_code

"""FastAPI backend for the Recipamatic API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from recipamatic.api.crud import recipe_list
from recipamatic.api.models import RecipeInfoMini, RecipeSource

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
    return recipe_list()

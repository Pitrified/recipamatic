"""FastAPI backend for the Recipamatic API."""

from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger as lg

from recipamatic.api.crud import (
    create_recipe_note,
    load_recipe,
    load_recipe_list,
    load_recipe_note,
)
from recipamatic.api.models import AudioFile, RecipeInfoMini
from recipamatic.cook.recipe_core.recipe_core import RecipeCore
from recipamatic.cook.recipe_note.model import RecipeNote

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


@app.get("/recipe_note/{code}/show", response_model=RecipeNote)
async def get_recipe_note(code: str) -> RecipeNote:
    """Endpoint to get a recipe note by code."""
    lg.debug(f"get_recipe_note: code={code}")
    recipe_note = load_recipe_note(code)
    if recipe_note is None:
        raise HTTPException(status_code=404, detail="Recipe note not found")
    return recipe_note


@app.post("/recipe_note_create", response_model=str)
async def create_note() -> str:
    """Endpoint to create a new recipe note."""
    lg.debug(f"create_note")
    note_code = create_recipe_note()
    return note_code


@app.post("/recipe_note/{code}/update", response_model=RecipeNote)
async def update_note(
    code: str,
    audio_file: UploadFile,
) -> RecipeNote:
    """Endpoint to update a recipe note."""

    # Read the file content as binary
    file_content = await audio_file.read()

    if audio_file.filename is None or audio_file.content_type is None:
        raise HTTPException(
            status_code=400, detail="Filename and content type are required"
        )

    # Populate the Pydantic model
    file_details = AudioFile(
        filename=audio_file.filename,
        content_type=audio_file.content_type,
        size=len(file_content),
        content=file_content,
    )
    lg.debug(f"update_note {code} {file_details.filename} {file_details.size}")

    # parse the model
    # TODO
    # whisperer
    # update the note

    return RecipeNote()

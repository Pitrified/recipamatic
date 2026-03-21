"""FastAPI backend for the Recipamatic API."""

from fastapi import Depends, FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger as lg
from recipamatic.api.crud import (
    create_recipe_note,
    load_recipe,
    load_recipe_list,
    load_recipe_note,
    load_recipe_note_holder,
)
from recipamatic.api.models import AudioFile, RecipeInfoMini
from recipamatic.auth.dependencies import get_current_active_user, get_current_user
from recipamatic.auth.models import User
from recipamatic.auth.router import router as auth_router
from recipamatic.cook.recipe_core.recipe_core import RecipeCore
from recipamatic.cook.recipe_note.model import RecipeNote
from recipamatic.whisperer.whisperer import Whisperer

app = FastAPI(title="Recipamatic API", version="1.0.0")


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

# Include the authentication router
app.include_router(auth_router)


@app.get("/recipe_list", response_model=list[RecipeInfoMini])
async def get_recipe_list(
    current_user: User = Depends(get_current_user),
) -> list[RecipeInfoMini]:
    """Endpoint to get the list of recipes.

    If user is authenticated, returns only their recipes.
    If not authenticated, returns public recipes.
    """
    lg.debug(
        f"get_recipe_list for user: {current_user.id if current_user else 'anonymous'}"
    )
    return load_recipe_list(user_id=current_user.id if current_user else None)


@app.get("/recipes/{code}/show", response_model=RecipeCore)
async def show_recipe(
    code: str, current_user: User = Depends(get_current_user)
) -> RecipeCore:
    """Endpoint to get a specific recipe by code."""
    lg.debug(
        f"show_recipe: code={code}, user={current_user.id if current_user else 'anonymous'}"
    )
    recipe = load_recipe(code)

    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    # Check if the recipe is public or owned by the current user
    if recipe.user_id and recipe.user_id != getattr(current_user, "id", None):
        raise HTTPException(status_code=403, detail="Access denied")

    return recipe


@app.get("/recipe_note/{code}/show", response_model=RecipeNote)
async def get_recipe_note(
    code: str, current_user: User = Depends(get_current_active_user)
) -> RecipeNote:
    """Endpoint to get a recipe note by code. Requires authentication."""
    lg.debug(f"get_recipe_note: code={code}, user={current_user.id}")
    recipe_note = load_recipe_note(code)

    if recipe_note is None:
        raise HTTPException(status_code=404, detail="Recipe note not found")

    # Check if the note is owned by the current user
    if recipe_note.user_id and recipe_note.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access denied")

    return recipe_note


@app.post("/recipe_note/create", response_model=str)
async def create_note(current_user: User = Depends(get_current_active_user)) -> str:
    """Endpoint to create a new recipe note. Requires authentication."""
    lg.debug(f"create_note for user: {current_user.id}")
    note_code = create_recipe_note(user_id=current_user.id)
    return note_code


@app.post("/recipe_note/{code}/update", response_model=RecipeNote)
async def update_note(
    code: str,
    audio_file: UploadFile,
    current_user: User = Depends(get_current_active_user),
) -> RecipeNote:
    """Endpoint to update a recipe note. Requires authentication."""

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
    lg.debug(
        f"update_note {code} {file_details.filename} {file_details.size} {file_details.content_type} for user {current_user.id}"
    )

    # load the note
    rnh = load_recipe_note_holder(code)
    if rnh is None:
        raise HTTPException(status_code=404, detail="Recipe note not found")

    recipe_note = rnh.note

    # Check if the note is owned by the current user
    if recipe_note.user_id and recipe_note.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access denied")

    # transcribe with whisperer
    whisperer = Whisperer()
    text = whisperer.extract_text_from_audio_file(file_details)
    lg.debug(f"Extracted text: {text}")

    # update the note
    recipe_note.add_note(text)
    lg.debug(f"Updated note: {recipe_note}")
    # save the note
    rnh.save_note()

    return recipe_note

# Foundation

## System Architecture

Recipamatic is built with a Python backend and Svelte frontend architecture:

- **Backend (Python)**: Handles data processing, recipe parsing, audio transcription, and social media integration
- **Frontend (SvelteKit)**: Provides user interface for viewing recipes, creating notes, and recording audio

## Core Data Flow

1. Recipe data can be ingested from:
   - Audio recordings (transcribed with Whisper)
   - Instagram posts
   - Manual entry
2. Data is stored in JSON format in the filesystem:
   - Recipe notes: `/data/notes/`
   - Recipes: `/data/recipes/`
   - Instagram data: `/data/ig/`

## Configuration System

The application uses a singleton configuration pattern to manage paths and settings across the application, defined in `py/src/recipamatic/config/recipamatic_config.py`.

The key configuration components include:

- `RecipamaticConfig`: Singleton class for application-wide configuration
- `RecipamaticPaths`: Manages file paths for data storage and source code

## Key Entry Points

- **Backend API**: The FastAPI server defined in `py/src/recipamatic/api/backend.py` serves as the main entry point for the frontend to interact with the backend.
- **Frontend App**: The SvelteKit application in `sv/src/` defines the user interface and interaction flow.

## Data Models

The core data models are defined in:

- `py/src/recipamatic/cook/recipe_core/recipe_core.py` - Recipe structure
- `py/src/recipamatic/cook/recipe_note/model.py` - Note taking structure

See [Recipe Core](./2-recipe-core.md) for more details on these data models.

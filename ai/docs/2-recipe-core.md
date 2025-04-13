# Recipe Core

## Data Models

The core recipe data model is defined in `py/src/recipamatic/cook/recipe_core/recipe_core.py`:

- `RecipeCore`: Container for a complete recipe with:
  - Name
  - List of preparations
  - Optional notes
- `Preparation`: Section of a recipe with:
  - Optional preparation name
  - List of ingredients
  - List of steps
- `Ingredient`: Single ingredient with:
  - Name
  - Quantity
- `Step`: Instruction step with:
  - Type (currently only "text" is supported)
  - Instruction text

## Recipe Processing Components

Recipes are managed through several key components:

### Recipe Core Transcriber

The `RecipeCoreTranscriber` class in `py/src/recipamatic/cook/recipe_core/transcriber.py` converts text descriptions to structured `RecipeCore` objects using an LLM.

Key aspects:

- Uses ChatOpenAI to analyze and structure recipe text
- Extracts ingredients, steps, and preparation sections
- Organizes information into the RecipeCore model format

### Recipe Core Editor

The `RecipeCoreEditor` class in `py/src/recipamatic/cook/recipe_core/editor.py` allows for updating specific parts of a recipe:

- Updates individual steps while preserving the rest of the recipe
- Uses an LLM to understand natural language edit instructions
- Returns a new RecipeCore with the specified changes

### Section Index Finder

The `SectionIdxFinder` class in `py/src/recipamatic/cook/recipe_core/section_idx_finder.py` helps locate specific sections in a recipe:

- Interprets natural language queries about recipe sections
- Returns references to specific preparation and step indices
- Enables targeted editing of recipe components

### Recipe Core Holder

The `RecipeCoreHolder` class in `py/src/recipamatic/cook/recipe_core/holder.py` manages recipe storage:

- Handles loading/saving recipes to the filesystem
- Generates and tracks recipe codes
- Manages recipe file paths

## Data Flow for Recipe Creation

1. Raw recipe text is obtained (from transcription, social media, etc.)
2. RecipeCoreTranscriber converts text to a structured RecipeCore object
3. RecipeCoreHolder saves the recipe to disk with a unique code
4. Frontend can access the recipe via the API

## Related Components

- [Audio Transcription](./4-audio-transcription.md) discusses how audio notes are converted to RecipeNotes
- [Social Integration](./3-social-integration.md) explains how recipes are extracted from Instagram posts

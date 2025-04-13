# Audio Transcription

## Overview

Recipamatic enables users to record and transcribe audio notes while cooking, which can later be converted into structured recipes. This feature is particularly useful for capturing cooking steps in real-time without needing to touch a screen or keyboard.

## Key Components

### Whisperer

The `Whisperer` class in `py/src/recipamatic/whisperer/whisperer.py` provides the core speech-to-text functionality:

- Wraps OpenAI's Whisper model for audio transcription
- Supports multiple languages and accents
- Allows for different model sizes based on accuracy needs (base, medium, large)
- Handles audio file processing and extraction

### Recipe Notes

The recipe note functionality is implemented through several components:

#### Recipe Note Model

Defined in `py/src/recipamatic/cook/recipe_note/model.py`:

- `RecipeNote`: Container for a series of timestamped notes

  - Tracks the start time of the note-taking session
  - Contains a list of individual notes
  - Provides methods for adding notes and formatting

- `Note`: Individual note entry with:
  - Text content (transcribed from audio)
  - Timestamp relative to the start of the session

#### Recipe Note Holder

The `RecipeNoteHolder` class in `py/src/recipamatic/cook/recipe_note/holder.py` manages note storage:

- Generates unique note codes based on timestamps
- Handles loading and saving notes to the filesystem
- Creates new note sessions on demand

### API Integration

Audio recording and processing is exposed through the FastAPI backend:

- `/recipe_note/create` endpoint creates a new note session
- `/recipe_note/{code}/update` endpoint accepts audio uploads and transcribes them
- `/recipe_note/{code}/show` endpoint retrieves existing notes

## User Flow for Audio Transcription

1. User initiates a new recipe note session from the frontend
2. The backend creates a new RecipeNote with a unique code
3. The user records audio snippets while cooking
4. Each recording is sent to the backend, transcribed by Whisper, and added to the note
5. The complete set of notes can later be converted to a structured recipe

## Frontend Components

The audio recording functionality is implemented in the `AudioRecorder.svelte` component in `sv/src/components/audio/AudioRecorder.svelte`:

- Handles browser audio recording permissions
- Manages recording state (start/stop)
- Packages audio data for transmission to the backend
- Updates UI with transcription results

## Recipe Creation from Notes

After recording notes, they can be converted to a structured recipe:

1. The complete note transcript is processed by the RecipeCoreTranscriber
2. A new RecipeCore is created with structured ingredients and steps
3. The recipe is saved with a code that references the original note

This workflow is demonstrated in the notebook `py/scratch_space/recipe_core_/create_from_note.ipynb`.

## Related Components

- [Foundation](./1-foundation.md) provides context on the overall system architecture
- [Recipe Core](./2-recipe-core.md) explains how transcribed notes are converted to recipes

# Frontend

## Overview

Recipamatic's frontend is built with SvelteKit, providing a responsive and interactive user interface for recipe management, viewing, and audio recording. The frontend communicates with the Python backend through a REST API.

## Key Components

### Core Routes

The application's main routes are defined in `sv/src/routes/`:

- `/` - Home page with navigation options
- `/recipes` - List of all available recipes
- `/recipes/[code]/show` - Detailed view of a specific recipe
- `/recipe_note/[code]/show` - View of a recipe note with audio recording functionality

### Recipe Components

#### Recipe List

The `RecipeList.svelte` component in `sv/src/components/RecipeList.svelte`:

- Fetches and displays all available recipes
- Handles loading states and error conditions
- Renders recipe cards for navigation

#### Recipe Card

The `RecipeCard.svelte` component in `sv/src/components/RecipeCard.svelte`:

- Displays a compact view of a recipe
- Shows recipe name, source, and code
- Links to the detailed recipe view

#### Recipe Show

The `RecipeShow.svelte` component in `sv/src/components/recipe_core/RecipeShow.svelte`:

- Renders the complete recipe with all preparations
- Displays ingredients and steps in a structured format
- Shows recipe notes if available

### Recipe Note Components

#### Recipe Note Show

The `RecipeNoteShow.svelte` component in `sv/src/components/recipe_note/RecipeNoteShow.svelte`:

- Displays a recipe note with timestamps
- Shows the transcribed text from audio recordings
- Formats the note in a readable way

#### Audio Recorder

The `AudioRecorder.svelte` component in `sv/src/components/audio/AudioRecorder.svelte`:

- Provides UI for recording audio notes
- Handles browser audio recording API interactions
- Sends recorded audio to the backend for transcription
- Updates the UI when new transcriptions are available

### Data Models

The frontend uses TypeScript interfaces to define data structures:

- `RecipeCore` in `sv/src/lib/models/recipe_core.ts` - Structure of a complete recipe
- `RecipeNote` in `sv/src/lib/models/recipe_note.ts` - Structure of recipe notes with timestamps
- `RecipeInfoMini` in `sv/src/lib/types.ts` - Minimal recipe information for listings

### API Communication

The frontend communicates with the backend using the Fetch API:

- API endpoints are configured with a base URL from `sv/src/lib/constants.ts`
- Error handling and loading states are managed at the component level
- API responses are typed using the TypeScript interfaces

## User Flows

### Viewing Recipes

1. User navigates to the `/recipes` route
2. The `RecipeList` component fetches all available recipes
3. User selects a recipe to view details
4. The `RecipeShow` component renders the complete recipe

### Recording Recipe Notes

1. User clicks "New Recipe Note" button on the home page
2. The backend creates a new note and returns a unique code
3. User is redirected to the note view page
4. The `AudioRecorder` component allows recording audio snippets
5. Recorded snippets are transcribed and added to the note
6. The note is displayed in real-time as it's updated

## Styling and Layout

The frontend uses simple, clean styling with:

- Card-based layouts for recipe lists
- Structured formatting for recipe details
- Clear typography for readability
- Responsive design for mobile and desktop use

## Related Components

- [Foundation](./1-foundation.md) provides context on the overall system architecture
- [Audio Transcription](./4-audio-transcription.md) details the backend processing of audio recordings

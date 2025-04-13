# Recipamatic Documentation

These documents summarize the implementation details for each component of the Recipamatic application.

## Inspiration

This documentation structure is inspired by and based on [envelope-budgeting-test documentation](https://github.com/vincanger/envelope-budgeting-test/tree/main/ai/docs). Special thanks to the creators of that project for providing an excellent template for LLM-friendly documentation.

## Documentation Principles

- **Single Source of Truth**:

  - The Python data models in `py/src/recipamatic/cook/recipe_core/recipe_core.py` and `py/src/recipamatic/cook/recipe_note/model.py` are the definitive sources for all recipe data models. Documentation should reference these models but not duplicate their definitions.
  - The Svelte components and routes in `sv/src/routes` and `sv/src/components` define the frontend structure.

- **Avoid Redundancy**:

  - Do not include lengthy code excerpts directly within these markdown files. Instead, describe the functionality and point to the relevant source code files.

- **Cross-Referencing**:

  - Link between related documentation files. For example, the recipe transcription documentation should link to the audio processing and social media documentation where relevant.

- **Focus on Overview & Context**:
  - These documents should provide a high-level summary of what was implemented, why certain decisions were made, key challenges encountered, and how components interconnect.

## How to maintain these documents

When implementing new features, this documentation structure allows for easy updates:

1. Create a new documentation file if adding a major component
2. Update cross-references in related files
3. Ensure the documentation follows the established principles

## Documentation Files

1. [Foundation](./1-foundation.md) - Core system architecture and data models
2. [Recipe Core](./2-recipe-core.md) - Recipe data structures and processing
3. [Social Integration](./3-social-integration.md) - Instagram and other social media integrations
4. [Audio Transcription](./4-audio-transcription.md) - Voice recording and transcription functionality
5. [Frontend](./5-frontend.md) - Svelte frontend components and routes

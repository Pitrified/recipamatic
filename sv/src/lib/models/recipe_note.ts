export interface Note {
    /** Represents a note for a recipe. */
    text: string; // The text of the note.
    timestamp: Date; // The timestamp when the note was taken.
}

export interface RecipeNote {
    /** Represents a note for a recipe. */
    start_timestamp: Date; // The timestamp when the note was taken.
    notes: Note[]; // A list of notes for the recipe.
}
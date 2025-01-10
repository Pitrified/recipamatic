<script lang="ts">
    // import type { RecipeNote, Note } from '../../lib/models/recipe_note';
    import type { RecipeNote, Note } from '$lib/models/recipe_note';

    export let recipeNote: RecipeNote;
</script>

<style>
    .note {
        border: 1px solid #ccc;
        padding: 10px;
        margin-bottom: 10px;
    }
</style>

<div>
    <h2>Recipe Note</h2>
    <p><strong>Start Timestamp:</strong> {recipeNote.start_timestamp.toLocaleString()}</p>
    <h3>Notes:</h3>
    {#each recipeNote.notes as note}
        <div class="note">
            <p><strong>Text:</strong> {note.text}</p>
            <p><strong>Timestamp:</strong> {note.timestamp.toLocaleString()}</p>
        </div>
    {/each}
</div>
<script lang="ts">
  import { goto } from '$app/navigation';
  import { API_BASE_URL } from '$lib/constants';

  async function createRecipeNote(event: MouseEvent) {
    event.preventDefault();
    try {
      const response = await fetch(`${API_BASE_URL}/recipe_note/create`, {
        method: 'POST'
      });
      if (!response.ok) {
        console.error('Error creating recipe note');
        return;
      }
      const rawNoteCode = await response.text();
      // Remove quotes from the returned code
      const noteCode = JSON.parse(rawNoteCode);
      console.log('new note code:', noteCode);
      goto(`/recipe_note/${noteCode}/show`);
    } catch (err) {
      console.error(err);
    }
  }
</script>

<nav>
  <a href="/">Home</a>
  <a href="/recipes">Recipes</a>
  <button on:click={createRecipeNote}>New Recipe Note</button>
</nav>

<slot />

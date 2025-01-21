<script lang="ts">
  import { page } from "$app/stores";
  import { onMount } from "svelte";
  import RecipeNoteShow from "$components/recipe_note/RecipeNoteShow.svelte";
  import type { RecipeNote } from "$lib/models/recipe_note";
  import { API_BASE_URL } from "$lib/constants";
  import AudioRecorder from "$components/audio/AudioRecorder.svelte";

  let recipeNote: RecipeNote | null = null;
  let error: string | null = null;

  // Access the route parameters
  $: code = $page.params.code;

  onMount(async () => {
    try {
      console.log("Fetching recipe note:", code);
      const response = await fetch(`${API_BASE_URL}/recipe_note/${code}/show`);
      if (!response.ok) {
        throw new Error("Failed to fetch recipe note");
      }
      recipeNote = await response.json();
    } catch (err) {
      console.error("Error loading recipe:", err);
      if (err instanceof Error) {
        error = err.message;
      } else {
        error = "An unknown error occurred:" + err;
      }
    }
  });
</script>

{#if recipeNote}
  <RecipeNoteShow {recipeNote} />
{:else if error}
  <p>{error}</p>
{:else}
  <p>Loading...</p>
{/if}

<!-- show an audio recorder button that sends to recipe_note/<code>/update -->
<AudioRecorder fetchUrl={`${API_BASE_URL}/recipe_note/${code}/update`} />

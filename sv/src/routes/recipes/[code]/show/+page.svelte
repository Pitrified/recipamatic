<!-- src/routes/recipes/[code]/show/+page.svelte -->
<script lang="ts">
  import { page } from "$app/stores";
  import { API_BASE_URL } from "$lib/constants";
  import type { RecipeCore } from "$lib/models/recipe_core";
  import { onMount } from "svelte";
  import RecipeShow from "$components/recipe_core/RecipeShow.svelte";

  let recipe: RecipeCore;
  let error: string | null = null;

  // Access the route parameters
  $: code = $page.params.code;

  onMount(async () => {
    try {
      console.log("Fetching recipe:", code);
      const response = await fetch(`${API_BASE_URL}/recipes/${code}/show`);
      if (!response.ok) {
        throw new Error(`Failed to fetch recipe: ${response.statusText}`);
      }
      recipe = await response.json();
    } catch (err) {
      console.error("Error loading recipe:", err);
      error = "Failed to load recipe";
    }
  });
</script>

{#if recipe}
  <RecipeShow {recipe} />
{:else if error}
  <p>{error}</p>
{:else}
  <p>Loading...</p>
{/if}

<style>
</style>

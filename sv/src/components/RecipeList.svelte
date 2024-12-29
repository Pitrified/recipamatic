<script lang="ts">
  import { onMount } from 'svelte';
  import RecipeCard from './RecipeCard.svelte';
  import { API_BASE_URL } from '$lib/constants';
  import type { RecipeInfoMini } from '$lib/types';

  let recipes: RecipeInfoMini[] = [];
  let error: string | null = null;
  let isLoading = true;

  // Fetch the recipe list from the API
  async function fetchRecipes() {
    try {
      const response = await fetch(`${API_BASE_URL}/recipe_list`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      recipes = await response.json();
    } catch (err) {
      error = err instanceof Error ? err.message : 'An unknown error occurred';
    } finally {
      isLoading = false;
    }
  }

  onMount(fetchRecipes);
</script>

<style>
  main {
    padding: 1rem;
    font-family: Arial, sans-serif;
  }

  .recipe-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
    padding: 1rem;
  }

  .error {
    color: red;
    font-weight: bold;
    text-align: center;
    margin-top: 2rem;
  }

  .loading {
    text-align: center;
    margin-top: 2rem;
    font-style: italic;
    color: #555;
  }
</style>

<main>
  {#if error}
    <p class="error">Error: {error}</p>
  {:else if isLoading}
    <p class="loading">Loading recipes...</p>
  {:else if recipes.length === 0}
    <p class="loading">No recipes found.</p>
  {:else}
    <div class="recipe-list">
      {#each recipes as recipe (recipe.code)}
        <RecipeCard {recipe} />
      {/each}
    </div>
  {/if}
</main>

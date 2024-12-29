<!-- src/routes/recipes/[code]/show/+page.svelte -->
<script lang="ts">
  import { page } from '$app/stores';
  import { API_BASE_URL } from '$lib/constants';
  import type { RecipeCore } from '$lib/models/recipe_core';
  import { onMount } from 'svelte';

  let recipe: RecipeCore;
  let error: string | null = null;

  // Access the route parameters
  $: code = $page.params.code;

  onMount(async () => {
    try {
      console.log('Fetching recipe:', code);
      const response = await fetch(`${API_BASE_URL}/recipes/${code}/show`);
      if (!response.ok) {
        throw new Error(`Failed to fetch recipe: ${response.statusText}`);
      }
      recipe = await response.json();
    } catch (err) {
      console.error('Error loading recipe:', err);
      error = 'Failed to load recipe';
    }
  });
</script>

<style>
  .recipe-details {
    padding: 1rem;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
</style>

{#if recipe}
  <div class="recipe-details">
    <h1>{recipe.name}</h1>
    {#each recipe.preparations as preparation}
      <h2>{preparation.preparation_name}</h2>
      <ul>
        {#each preparation.ingredients as ingredient}
          <li>{ingredient.name}: {ingredient.quantity}</li>
        {/each}
      </ul>
      <ol>
        {#each preparation.steps as step}
          <li>{step.instruction}</li>
        {/each}
      </ol>
    {/each}
    {#if recipe.notes}
      <h3>Notes</h3>
      <ul>
        {#each recipe.notes as note}
          <li>{note}</li>
        {/each}
      </ul>
    {/if}
  </div>
{:else if error}
  <p>{error}</p>
{:else}
  <p>Loading...</p>
{/if}
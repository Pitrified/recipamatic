<script lang="ts">
  import { onMount } from "svelte";
  import ProtectedRoute from "../../components/ProtectedRoute.svelte";
  import { fetchApiGet } from "$lib/utils/api";
  import type { RecipeInfoMini } from "$lib/types";

  let recipes: RecipeInfoMini[] = [];
  let loading = true;
  let error: string | null = null;

  onMount(async () => {
    try {
      loading = true;
      recipes = await fetchApiGet<RecipeInfoMini[]>("/recipe_list");
      // Filter to only show recipes owned by the current user
      recipes = recipes.filter((recipe) => recipe.user_id !== null);
    } catch (err) {
      console.error("Error loading recipes:", err);
      error = "Failed to load your recipes. Please try again later.";
    } finally {
      loading = false;
    }
  });
</script>

<ProtectedRoute>
  <div class="my-recipes">
    <h1>My Recipes</h1>

    {#if loading}
      <div class="loading">
        <div class="loading-spinner"></div>
        <p>Loading your recipes...</p>
      </div>
    {:else if error}
      <div class="error-message">
        <p>{error}</p>
        <button on:click={() => window.location.reload()}>Try Again</button>
      </div>
    {:else if recipes.length === 0}
      <div class="empty-state">
        <h2>No recipes yet</h2>
        <p>
          You haven't created any recipes yet. Start by creating a recipe note
          or importing from Instagram.
        </p>
        <div class="action-buttons">
          <a href="/recipe_note/create" class="button primary"
            >Create Recipe Note</a
          >
        </div>
      </div>
    {:else}
      <div class="recipe-grid">
        {#each recipes as recipe}
          <a href="/recipes/{recipe.code}/show" class="recipe-card">
            <div class="recipe-source {recipe.source}">{recipe.source}</div>
            <h2>{recipe.name}</h2>
            <div class="recipe-visibility">
              {recipe.is_public ? "Public" : "Private"}
            </div>
          </a>
        {/each}
      </div>
    {/if}
  </div>
</ProtectedRoute>

<style>
  .my-recipes {
    max-width: 1000px;
    margin: 0 auto;
  }

  h1 {
    margin-bottom: 2rem;
    color: #333;
  }

  .loading,
  .error-message,
  .empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 3rem;
    text-align: center;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .loading-spinner {
    width: 40px;
    height: 40px;
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-left-color: #4285f4;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 1rem;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  .error-message p {
    color: #d32f2f;
    margin-bottom: 1rem;
  }

  .empty-state h2 {
    margin-bottom: 1rem;
    color: #333;
  }

  .empty-state p {
    margin-bottom: 2rem;
    color: #666;
    max-width: 500px;
  }

  .action-buttons {
    display: flex;
    gap: 1rem;
  }

  .button {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    text-decoration: none;
    font-weight: 500;
    transition: background-color 0.2s;
  }

  .button.primary {
    background-color: #4285f4;
    color: white;
  }

  .button.primary:hover {
    background-color: #3367d6;
  }

  .recipe-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
  }

  .recipe-card {
    position: relative;
    padding: 1.5rem;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-decoration: none;
    color: #333;
    transition:
      transform 0.2s,
      box-shadow 0.2s;
  }

  .recipe-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  }

  .recipe-source {
    position: absolute;
    top: 0.75rem;
    right: 0.75rem;
    padding: 0.3rem 0.6rem;
    font-size: 0.75rem;
    border-radius: 4px;
    text-transform: uppercase;
    font-weight: 600;
  }

  .recipe-source.ig {
    background-color: #fbf0f0;
    color: #e4405f;
  }

  .recipe-source.note {
    background-color: #f0f8ff;
    color: #4285f4;
  }

  .recipe-source.manual {
    background-color: #f0f8ea;
    color: #34a853;
  }

  .recipe-card h2 {
    margin-top: 0.5rem;
    margin-bottom: 1.5rem;
    font-size: 1.3rem;
  }

  .recipe-visibility {
    font-size: 0.9rem;
    color: #666;
  }

  @media (max-width: 768px) {
    .recipe-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

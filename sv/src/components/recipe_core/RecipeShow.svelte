<script lang="ts">
  import Preparation from "./Preparation.svelte";

  export let recipe;
</script>

<div class="recipe-details">
  <h1>{recipe.name}</h1>
  {#each recipe.preparations as preparation}
    <Preparation {preparation} />
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

<style>
  .recipe-details {
    padding: 1rem;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
</style>

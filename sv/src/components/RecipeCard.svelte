<script>
  export let recipe;
</script>

<style>
  .recipe-card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background: #fff;
  }
  .recipe-name {
    font-size: 1.25rem;
    font-weight: bold;
  }
  .recipe-source {
    font-style: italic;
    color: #555;
  }
  .recipe-code {
    font-family: monospace;
    color: #333;
  }
</style>

<div class="recipe-card">
  <div class="recipe-name">{recipe.name}</div>
  <div class="recipe-source">Source: {recipe.source}</div>
  <div class="recipe-code">Code: {recipe.code}</div>
</div>

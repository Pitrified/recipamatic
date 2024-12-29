<script lang="ts">
  export let ingredients;
</script>

<ul>
  {#each ingredients as ingredient}
    <li>{ingredient.name}: {ingredient.quantity}</li>
  {/each}
</ul>
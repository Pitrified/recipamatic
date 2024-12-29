<script lang="ts">
  import type { Preparation_m } from "$lib/models/recipe_core";
  import Steps from "../Steps.svelte";
  import Ingredients from "./Ingredients.svelte";

  export let preparation: Preparation_m;
  let ingredients = preparation.ingredients;
  let steps = preparation.steps;
</script>

<h2>{preparation.preparation_name}</h2>
<Ingredients {ingredients} />
<Steps {steps} />
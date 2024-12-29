<script lang="ts">
  export let steps;
</script>

<ol>
  {#each steps as step}
    <li>{step.instruction}</li>
  {/each}
</ol>
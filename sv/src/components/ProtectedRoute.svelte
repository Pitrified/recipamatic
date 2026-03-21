<script lang="ts">
  import { isAuthenticated } from "$lib/stores/auth";
  import { onMount } from "svelte";
  import { goto } from "$app/navigation";

  export let redirectTo = "/login";

  onMount(() => {
    // Subscribe to authentication state
    const unsubscribe = isAuthenticated.subscribe((value) => {
      if (!value) {
        // If not authenticated, redirect to login page
        goto(redirectTo);
      }
    });

    // Cleanup subscription on component unmount
    return () => {
      unsubscribe();
    };
  });
</script>

{#if $isAuthenticated}
  <slot />
{:else}
  <div class="loading-container">
    <div class="loading-spinner"></div>
    <p>Checking authentication...</p>
  </div>
{/if}

<style>
  .loading-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 70vh;
  }

  .loading-spinner {
    width: 30px;
    height: 30px;
    border: 3px solid rgba(0, 0, 0, 0.1);
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

  p {
    color: #666;
  }
</style>

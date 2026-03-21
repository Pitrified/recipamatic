<script lang="ts">
  import { onMount } from "svelte";
  import { goto } from "$app/navigation";
  import { handleAuthCallback } from "$lib/stores/auth";

  // This component handles the OAuth callback and extracts the token from the URL
  onMount(() => {
    const params = new URLSearchParams(window.location.search);
    const token = params.get("token");
    const error = params.get("error");

    if (token) {
      // Store the token and redirect to recipes page
      handleAuthCallback(token);
      goto("/recipes");
    } else if (error) {
      // Handle authentication error
      console.error("Authentication error:", error);
      goto("/login?error=" + error);
    } else {
      // No token or error, redirect to login
      goto("/login");
    }
  });
</script>

<div class="callback-container">
  <div class="loading-spinner"></div>
  <p>Completing authentication, please wait...</p>
</div>

<style>
  .callback-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    text-align: center;
    padding: 0 1rem;
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

  p {
    color: #666;
    font-size: 1.1rem;
  }
</style>

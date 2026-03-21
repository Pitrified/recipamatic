<script lang="ts">
  import { onMount } from "svelte";
  import { fetchUserProfile } from "$lib/stores/auth";
  import Nav from "../components/Nav.svelte";

  // Fetch user profile on app start if there's a token in localStorage
  onMount(() => {
    fetchUserProfile();
  });
</script>

<div class="app">
  <Nav />
  <main>
    <slot />
  </main>
  <footer>
    <p>© 2025 Recipamatic - A recipe management application</p>
  </footer>
</div>

<style>
  :global(body) {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    background-color: #f9f9f9;
  }

  .app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  main {
    flex: 1;
    padding: 2rem;
    max-width: 1200px;
    margin: 0 auto;
    width: 100%;
  }

  footer {
    background-color: #f1f1f1;
    padding: 1rem;
    text-align: center;
    margin-top: auto;
  }

  footer p {
    margin: 0;
    color: #666;
    font-size: 0.9rem;
  }

  @media (max-width: 768px) {
    main {
      padding: 1rem;
    }
  }
</style>

<script lang="ts">
  import { loginWithGoogle } from "$lib/stores/auth";
</script>

<div class="login-container">
  <div class="login-card">
    <h1>Welcome to Recipamatic</h1>
    <p>Sign in to manage your recipes, create new ones, and more.</p>

    <div class="login-options">
      <button class="login-button google" on:click={loginWithGoogle}>
        <img
          src="/images/google-icon.svg"
          alt="Google logo"
          width="20"
          height="20"
        />
        Sign in with Google
      </button>
    </div>
  </div>
</div>

<style>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 80vh;
    padding: 1rem;
  }

  .login-card {
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 2rem;
    max-width: 400px;
    text-align: center;
  }

  h1 {
    margin-bottom: 1rem;
    color: #333;
  }

  p {
    margin-bottom: 2rem;
    color: #666;
  }

  .login-options {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .login-button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
    border-radius: 4px;
    border: 1px solid #ddd;
    background-color: white;
    cursor: pointer;
    font-weight: 500;
    transition:
      background-color 0.2s,
      box-shadow 0.2s;
  }

  .login-button:hover {
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .login-button.google {
    border-color: #4285f4;
    color: #4285f4;
  }

  .login-button.google:hover {
    background-color: #f8f9fa;
  }
</style>

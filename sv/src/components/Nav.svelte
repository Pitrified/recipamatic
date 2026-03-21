<script lang="ts">
  import { isAuthenticated, user, logout } from "$lib/stores/auth";
  import { onMount } from "svelte";

  let userMenuOpen = false;

  // Toggle the user menu dropdown
  function toggleUserMenu() {
    userMenuOpen = !userMenuOpen;
  }

  // Close the menu when clicking outside
  function handleClickOutside(event: MouseEvent) {
    const target = event.target as HTMLElement;
    const userMenu = document.querySelector(".user-menu");

    if (userMenu && !userMenu.contains(target) && userMenuOpen) {
      userMenuOpen = false;
    }
  }

  onMount(() => {
    document.addEventListener("click", handleClickOutside);

    return () => {
      document.removeEventListener("click", handleClickOutside);
    };
  });
</script>

<nav class="main-nav">
  <div class="nav-logo">
    <a href="/">Recipamatic</a>
  </div>

  <div class="nav-links">
    <a href="/recipes">Recipes</a>
    {#if $isAuthenticated}
      <a href="/recipe_note/create">New Recipe Note</a>
    {/if}
  </div>

  <div class="nav-auth">
    {#if $isAuthenticated && $user}
      <div class="user-menu-container">
        <button class="user-avatar" on:click={toggleUserMenu}>
          {#if $user.picture}
            <img src={$user.picture} alt="User avatar" />
          {:else}
            <div class="avatar-placeholder">{$user.name.charAt(0)}</div>
          {/if}
        </button>

        {#if userMenuOpen}
          <div class="user-menu">
            <div class="user-info">
              <p class="user-name">{$user.name}</p>
              <p class="user-email">{$user.email}</p>
            </div>
            <div class="menu-divider"></div>
            <a href="/profile" class="menu-item">Profile</a>
            <a href="/my-recipes" class="menu-item">My Recipes</a>
            <button class="menu-item logout" on:click={logout}>Log out</button>
          </div>
        {/if}
      </div>
    {:else}
      <a href="/login" class="login-button">Log in</a>
    {/if}
  </div>
</nav>

<style>
  .main-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 2rem;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .nav-logo a {
    font-size: 1.5rem;
    font-weight: 700;
    color: #333;
    text-decoration: none;
  }

  .nav-links {
    display: flex;
    gap: 1.5rem;
  }

  .nav-links a {
    color: #555;
    text-decoration: none;
    transition: color 0.2s;
  }

  .nav-links a:hover {
    color: #4285f4;
  }

  .login-button {
    display: inline-block;
    padding: 0.5rem 1rem;
    background-color: #4285f4;
    color: white;
    border-radius: 4px;
    text-decoration: none;
    font-weight: 500;
    transition: background-color 0.2s;
  }

  .login-button:hover {
    background-color: #3367d6;
  }

  .user-menu-container {
    position: relative;
  }

  .user-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: none;
    cursor: pointer;
    overflow: hidden;
    padding: 0;
    background: none;
  }

  .user-avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .avatar-placeholder {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #4285f4;
    color: white;
    font-weight: 600;
    font-size: 1.2rem;
  }

  .user-menu {
    position: absolute;
    top: 50px;
    right: 0;
    width: 220px;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    z-index: 100;
  }

  .user-info {
    padding: 1rem;
  }

  .user-name {
    font-weight: 600;
    margin: 0 0 0.25rem 0;
    color: #333;
  }

  .user-email {
    font-size: 0.85rem;
    margin: 0;
    color: #666;
  }

  .menu-divider {
    height: 1px;
    background-color: #eee;
    margin: 0.5rem 0;
  }

  .menu-item {
    display: block;
    padding: 0.75rem 1rem;
    color: #333;
    text-decoration: none;
    transition: background-color 0.2s;
  }

  .menu-item:hover {
    background-color: #f5f5f5;
  }

  .menu-item.logout {
    color: #d32f2f;
    width: 100%;
    text-align: left;
    border: none;
    background: none;
    cursor: pointer;
    font-size: 1rem;
  }

  @media (max-width: 768px) {
    .main-nav {
      padding: 1rem;
    }

    .nav-links {
      gap: 1rem;
    }
  }
</style>

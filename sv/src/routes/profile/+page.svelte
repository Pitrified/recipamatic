<script lang="ts">
  import ProtectedRoute from "../../components/ProtectedRoute.svelte";
  import { user } from "$lib/stores/auth";

  // Format date for better readability
  function formatDate(dateString: string | undefined): string {
    if (!dateString) return "Never";

    const date = new Date(dateString);
    return new Intl.DateTimeFormat("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    }).format(date);
  }
</script>

<ProtectedRoute>
  <div class="profile-container">
    <div class="profile-header">
      <h1>Your Profile</h1>
      {#if $user?.picture}
        <img src={$user.picture} alt="Profile picture" class="profile-image" />
      {:else}
        <div class="profile-avatar">{$user?.name.charAt(0)}</div>
      {/if}
    </div>

    <div class="profile-details">
      <div class="detail-group">
        <h2>Account Information</h2>
        <div class="detail-item">
          <div class="detail-label">Name</div>
          <div class="detail-value">{$user?.name}</div>
        </div>
        <div class="detail-item">
          <div class="detail-label">Email</div>
          <div class="detail-value">{$user?.email}</div>
        </div>
        <div class="detail-item">
          <div class="detail-label">Account Type</div>
          <div class="detail-value">{$user?.role}</div>
        </div>
        <div class="detail-item">
          <div class="detail-label">Member Since</div>
          <div class="detail-value">{formatDate($user?.created_at)}</div>
        </div>
        <div class="detail-item">
          <div class="detail-label">Last Login</div>
          <div class="detail-value">{formatDate($user?.last_login)}</div>
        </div>
      </div>
    </div>
  </div>
</ProtectedRoute>

<style>
  .profile-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .profile-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #eee;
  }

  .profile-image {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
  }

  .profile-avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background-color: #4285f4;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.5rem;
    font-weight: 600;
  }

  .detail-group {
    margin-bottom: 2rem;
  }

  .detail-group h2 {
    margin-bottom: 1rem;
    font-size: 1.5rem;
    color: #333;
  }

  .detail-item {
    display: flex;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #f5f5f5;
  }

  .detail-label {
    width: 30%;
    font-weight: 600;
    color: #555;
  }

  .detail-value {
    flex: 1;
    color: #333;
  }

  @media (max-width: 768px) {
    .profile-header {
      flex-direction: column;
      gap: 1rem;
      text-align: center;
    }

    .detail-item {
      flex-direction: column;
      gap: 0.25rem;
    }

    .detail-label {
      width: 100%;
    }
  }
</style>

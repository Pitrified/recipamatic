import { writable } from "svelte/store";
import { browser } from "$app/environment";
import type { User } from "$lib/models/user";

// Initialize the auth stores
export const token = writable<string | null>(
  browser ? localStorage.getItem("auth_token") : null
);
export const user = writable<User | null>(null);
export const isAuthenticated = writable<boolean>(false);

// Save token to localStorage when it changes
token.subscribe((value) => {
  if (browser && value) {
    localStorage.setItem("auth_token", value);
  } else if (browser && !value) {
    localStorage.removeItem("auth_token");
  }
});

// Update authentication state when token changes
token.subscribe((value) => {
  isAuthenticated.set(!!value);
});

/**
 * Handles login callback by storing the JWT token
 */
export function handleAuthCallback(tokenValue: string): void {
  token.set(tokenValue);
  fetchUserProfile();
}

/**
 * Fetch the user profile using the stored token
 */
export async function fetchUserProfile(): Promise<void> {
  const currentToken = localStorage.getItem("auth_token");
  if (!currentToken) {
    user.set(null);
    return;
  }

  try {
    const response = await fetch("/api/auth/me", {
      headers: {
        Authorization: `Bearer ${currentToken}`,
      },
    });

    if (response.ok) {
      const userData = await response.json();
      user.set(userData);
    } else {
      // If we get an error, the token might be invalid
      logout();
    }
  } catch (error) {
    console.error("Error fetching user profile", error);
    logout();
  }
}

/**
 * Logout the user by clearing the token
 */
export function logout(): void {
  token.set(null);
  user.set(null);
  if (browser) {
    window.location.href = "/";
  }
}

/**
 * Redirect to Google login
 */
export function loginWithGoogle(): void {
  if (browser) {
    window.location.href = "/api/auth/login/google";
  }
}

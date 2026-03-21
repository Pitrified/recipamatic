import { browser } from "$app/environment";

const API_BASE_URL = "/api";

/**
 * Make an authenticated API request
 *
 * @param endpoint - API endpoint without the base URL
 * @param options - Fetch options
 * @returns Promise with the fetch response
 */
export async function fetchApi(
  endpoint: string,
  options: RequestInit = {}
): Promise<Response> {
  // Get token from localStorage
  const token = browser ? localStorage.getItem("auth_token") : null;

  // Prepare headers with authentication if token exists
  const headers = {
    "Content-Type": "application/json",
    ...options.headers,
  };

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  // Make the request
  return fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers,
  });
}

/**
 * Make an authenticated GET request
 */
export async function fetchApiGet<T>(endpoint: string): Promise<T> {
  const response = await fetchApi(endpoint, { method: "GET" });

  if (!response.ok) {
    throw new Error(`API error: ${response.status} ${response.statusText}`);
  }

  return response.json();
}

/**
 * Make an authenticated POST request
 */
export async function fetchApiPost<T>(
  endpoint: string,
  data?: any
): Promise<T> {
  const options: RequestInit = {
    method: "POST",
    body: data ? JSON.stringify(data) : undefined,
  };

  const response = await fetchApi(endpoint, options);

  if (!response.ok) {
    throw new Error(`API error: ${response.status} ${response.statusText}`);
  }

  return response.json();
}

/**
 * Make a file upload request with authentication
 * This doesn't set Content-Type as the browser will set it with the boundary
 */
export async function uploadApiFile<T>(
  endpoint: string,
  formData: FormData
): Promise<T> {
  const token = browser ? localStorage.getItem("auth_token") : null;

  const headers: HeadersInit = {};
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    method: "POST",
    headers,
    body: formData,
  });

  if (!response.ok) {
    throw new Error(`API error: ${response.status} ${response.statusText}`);
  }

  return response.json();
}

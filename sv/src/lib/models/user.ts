export enum UserRole {
  ADMIN = "admin",
  USER = "user",
}

export interface User {
  id: string;
  email: string;
  name: string;
  picture?: string;
  role: UserRole;
  created_at: string;
  last_login?: string;
}

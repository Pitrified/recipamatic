export enum RecipeSource {
  IG = "ig",
  NOTE = "note",
  MANUAL = "manual",
}

export interface RecipeInfoMini {
  name: string;
  source: RecipeSource;
  code: string;
  user_id?: string;
  is_public: boolean;
}

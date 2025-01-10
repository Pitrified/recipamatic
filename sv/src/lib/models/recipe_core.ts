export interface Ingredient {
  /** The name of the ingredient. */
  name: string;
  /** The quantity of the ingredient. Includes both the amount and the unit. */
  quantity: string;
}

export enum StepType {
  TEXT = "text",
  // IMAGE = "image"
}

export interface Step {
  /** The type of step (e.g., 'text' or 'image'). */
  type: StepType;
  /** The explanation for this step, if text. */
  instruction?: string;
  // /** The filename of the image, if an image step. */
  // filename?: string;
  // /** A short description of the image content, for accessibility. */
  // alttext?: string;
}

export interface Preparation_m {
  /** The name of the preparation section. Can be None for the main preparation. */
  preparation_name?: string;
  /** A list of ingredients for this preparation. */
  ingredients: Ingredient[];
  /** A list of steps for this preparation. */
  steps: Step[];
}

export interface RecipeCore {
  /** The name of the recipe. */
  name: string;
  /** A list of preparation sections, each with ingredients and steps. */
  preparations: Preparation_m[];
  /** Optional notes for the recipe. */
  notes?: string[];
}
"""Convert a text recipe to a RecipeCore object."""

from dataclasses import dataclass

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate

from recipamatic.cook.recipe_core.recipe_core import RecipeCore
from recipamatic.langchain_openai_.chat_openai_config import ChatOpenAIConfig

transcriber_template = """You have a text recipe. \
You are an expert cook, but you are not pretentious.

Your task is to convert the text recipe into a list of ingredients and steps.
Follow the specified format.
Do not change the ingredients, quantities, or steps from the provided recipe.
Do not change the language of the recipe.

If the recipe is presented in several steps, you can combine the relevant ones into a single preparation.

The recipe is: {recipe}
"""

transcriber_prompt = ChatPromptTemplate(
    [SystemMessagePromptTemplate.from_template(transcriber_template)]
)


@dataclass
class RecipeCoreTranscriber:
    """Convert a text recipe to a RecipeCore object."""

    chat_openai_config: ChatOpenAIConfig

    def __post_init__(self):
        """Initialize the transcriber."""
        self.model = self.chat_openai_config.to_model()
        self.structured_llm = self.model.with_structured_output(RecipeCore)
        self.chain = transcriber_prompt | self.structured_llm

    def invoke(self, recipe: str) -> RecipeCore:
        """Convert a text recipe to a RecipeCore object."""
        output = self.chain.invoke({"recipe": recipe})
        if not isinstance(output, RecipeCore):
            raise ValueError(f"Unexpected output type: {type(output)}")
        return output

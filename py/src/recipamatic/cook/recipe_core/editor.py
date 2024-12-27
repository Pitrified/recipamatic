"""Edit a recipe."""

from dataclasses import dataclass

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from loguru import logger as lg

from recipamatic.cook.recipe_core.recipe_core import RecipeCore
from recipamatic.langchain_openai_.chat_openai_config import ChatOpenAIConfig

editor_template = """You have a recipe. \
You are an expert cook, but you are not pretentious.

The recipe is: {old_recipe}

This step is wrong: {old_step}

Please correct it keeping in mind that: {new_step}

Do not change the other steps.
Do not remove or edit the other preparations, return them unchanged.
"""

editor_prompt = ChatPromptTemplate(
    [SystemMessagePromptTemplate.from_template(editor_template)]
)


@dataclass
class RecipeCoreEditor:
    """Edit a recipe."""

    chat_openai_config: ChatOpenAIConfig

    def __post_init__(self):
        """Initialize the editor."""
        self.model = self.chat_openai_config.to_model()
        self.structured_llm = self.model.with_structured_output(RecipeCore)
        self.chain = editor_prompt | self.structured_llm

    def invoke(
        self,
        old_recipe: RecipeCore,
        old_step: str,
        new_step: str,
    ) -> RecipeCore:
        """Edit a recipe."""
        prompt_value = editor_prompt.invoke(
            {
                "old_recipe": old_recipe,
                "old_step": old_step,
                "new_step": new_step,
            }
        )
        lg.info(f"Prompt value: {prompt_value}")
        output = self.chain.invoke(
            {
                "old_recipe": old_recipe,
                "old_step": old_step,
                "new_step": new_step,
            }
        )
        if not isinstance(output, RecipeCore):
            raise ValueError(f"Unexpected output type: {type(output)}")
        return output

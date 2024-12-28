"""Find a section index in a RecipeCore object."""

from dataclasses import dataclass

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from loguru import logger as lg

from recipamatic.cook.recipe_core.section_idx import Section, SectionGen
from recipamatic.langchain_openai_.chat_openai_config import ChatOpenAIConfig

section_idx_template = """The user is editing a recipe. \
The user instruction identifies a section of the recipe.

User instruction: {user_instruction}

Extract the information required to identify the section:
* Preparation index
* Ingredient or step index
"""

section_idx_prompt = ChatPromptTemplate(
    [SystemMessagePromptTemplate.from_template(section_idx_template)]
)


@dataclass
class SectionIdxFinder:
    """Find a section index in a RecipeCore object."""

    chat_openai_config: ChatOpenAIConfig

    def __post_init__(self):
        """Initialize the section index finder."""
        self.model = self.chat_openai_config.to_model()
        self.structured_llm = self.model.with_structured_output(Section)
        self.chain = section_idx_prompt | self.structured_llm

    def invoke(
        self,
        user_instruction: str,
    ) -> SectionGen:
        """Find a section index in a RecipeCore object."""
        prompt_value = section_idx_prompt.invoke(
            {
                "user_instruction": user_instruction,
            }
        )
        lg.info(f"Prompt value: {prompt_value}")
        output = self.chain.invoke(
            {
                "user_instruction": user_instruction,
            }
        )
        if not isinstance(output, Section):
            lg.warning(f"Got {output} of type {type(output)}")
            raise ValueError(f"Expected output to be a Section, but got {type(output)}")
        return output.section

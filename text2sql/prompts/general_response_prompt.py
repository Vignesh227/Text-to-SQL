from text2sql.prompts.templates.general_response_template import general_response_template
from llama_index.core.prompts import PromptTemplate

GENERAL_RESPONSE_PROMPT  = PromptTemplate(
    general_response_template
)
from text2sql.prompts.templates.response_template import response_synthesis_template
from llama_index.core.prompts import PromptTemplate

RESPONSE_SYNTHESIS_PROMPT = PromptTemplate(
    response_synthesis_template
)
print("\n pipeline -> setup.py called \n")

from text2sql.core.retriever import (
    object_retriever, 
    sample_query_retriever, 
    sql_retriever
)
from text2sql.prompts.sql_prompt import (
    SQL_FAILURE_PROMPT,
    TEXT2SQL_PROMPT,
    SQL_FAILURE_PROMPT_TWO
)
from text2sql.prompts.response_prompt import RESPONSE_SYNTHESIS_PROMPT
from text2sql.prompts.general_response_prompt import GENERAL_RESPONSE_PROMPT
from text2sql.prompts.qn_classify_prompt import QUESTION_CLASSIFICATION_PROMPT


from text2sql.core.pipeline.workflows import TextToSQLWorkflow
from text2sql.core.ai_model.models import llm

text_to_sql_workflow = TextToSQLWorkflow(
    obj_retriever = object_retriever,
    sql_retriever = sql_retriever,
    sample_retriever=sample_query_retriever,
    text2sql_prompt = TEXT2SQL_PROMPT,
    response_synthesis_prompt= RESPONSE_SYNTHESIS_PROMPT,
    sql_failure_prompt = SQL_FAILURE_PROMPT,
    sql_failure_prompt_two = SQL_FAILURE_PROMPT_TWO,
    llm = llm,
    query_classification_prompt = QUESTION_CLASSIFICATION_PROMPT,
    general_response_prompt = GENERAL_RESPONSE_PROMPT,
    # verbose = True,
    timeout = 240
)
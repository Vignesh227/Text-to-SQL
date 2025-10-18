from text2sql.prompts.templates.sql_template import (
    sql_failure_template,
    sql_failure_template_two,
    text2sql_template
)
from text2sql.core.database.setup import db_conn

from llama_index.core.prompts import PromptTemplate


TEXT2SQL_PROMPT = PromptTemplate(
    text2sql_template
).partial_format(dialect = db_conn.engine.dialect.name)

# SAMPLE_RETRIEVE_PROMPT = PromptTemplate(
#     sample_retrieve_template
# ).partial_format(dialect = db_conn.dialect.name)

#Need to change this to above code later
# SAMPLE_RETRIEVE_PROMPT = sample_retrieve_template

SQL_FAILURE_PROMPT = PromptTemplate(
    sql_failure_template
).partial_format(dialect = db_conn.engine.dialect.name)


SQL_FAILURE_PROMPT_TWO = PromptTemplate(
    sql_failure_template_two
).partial_format(dialect = db_conn.engine.dialect.name)
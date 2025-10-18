from text2sql.prompts.templates.qn_classify_template import question_classification_template
from llama_index.core.prompts import PromptTemplate
from text2sql.core.database.setup import db_conn

QUESTION_CLASSIFICATION_PROMPT = PromptTemplate(
    question_classification_template
).partial_format(dialect = db_conn.engine.dialect.name)
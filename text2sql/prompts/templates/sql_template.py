text2sql_template = """
Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer. You can order the results by a relevant column to return the most interesting examples in the database.

Never query for all the columns from a specific table, only ask for a few relevant columns given the question.

Pay attention to use only the column names that you can see in the schema description. Be careful to not query for columns that do not exist. Pay attention to which column is in which table. Also, qualify column names with the table name when needed. You are required to use the following format, each taking one line:

If query generation seems inappropriate or irrelavant for the given question, then generate a simple text response for the user query.

Question: Question here
SQLQuery: SQL Query to run

Only use tables listed below and context is also provide below.
{schema}

Few sample questions are given below:
{sample_queries}

The below is the chat history: 
{chat_history_str}

Question: {query_str}
SQLQuery:
"""

# sql_failure_template = """
# Given the query : {query_str}, for {dialect} database, the sql query "{sql_query_str}" failed with the following error: {error}

# # You are required to use the following format, each taking one line:

# # Question: Question here
# # SQLQuery: SQL Query to run
# # SQLResult: Result of the SQLQuery
# # Answer: Final answer here

# If needed, refer previous chat history : {chat_history_str}

# Question: {query_str}
# SQLQuery:
# """

sql_failure_template = """
This is a Text to SQL application, developed by Coats Organization.

Use {dialect} database, with provided table context : {table_context_str}

Given the question : {query_str}, the generated sql query "{sql_query_str}" failed with the following error: {error}

You are required to use the following format, each taking one line:

Question: Question here
SQLQuery: SQL Query to run
SQLResult: Result of the SQLQuery
Answer: Final answer here

If needed, refer previous chat history : {chat_history_str}

Question: {query_str}
SQLQuery:
"""




sql_failure_template_two = """
This is an Text to SQL Application, developed by Coats Organization.

Use {dialect} database, with provided table context : {table_context_str}

Given the question : {query_str}, the generated sql query "{sql_query_str}" failed with the following error: {error}

Based on the user question, give a proper response to the user.

If needed, refer previous chat history : {chat_history_str}

Question: {query_str}
Response:

"""
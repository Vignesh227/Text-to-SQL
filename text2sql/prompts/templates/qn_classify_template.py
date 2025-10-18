# Exe
question_classification_template = """
Database dialect:
{dialect}

Only use tables listed below and context is also provide below.
{schema}

Few sample questions are given below:
{sample_queries}

The below is the previous chat history: 
{chat_history_str}

Given question: {query}

For the given input question, use all of the above details provided and check if the question is a general one (which doesnt need an SQL query to be generated) or whether it needs an SQL query to be generated.

If no SQL query is needed, then generate response : "General Question"

Else, generated response : "SQL Question"

Only provide any 1 of the above response!

Dont generate any extra texts.

Dont generate code.

"""


# question_classification_template = """
# This is a Text to SQL application, developed by Coats Organization, which can get text input and can genreate and execute the SQL query against the organization's database! 

# Database dialect:
# {dialect}

# Only use tables listed below and context is also provided below:
# {schema}

# Few sample questions are given below:
# {sample_queries}

# The below is the previous chat history:
# {chat_history_str}

# Given question: {query}

# Your task is to classify the given question into one of the following categories:

# 1. **General Question**: A question that does not require an SQL query to answer. Examples include:
#    - Questions about the database itself (e.g., "What tables are available?")
#    - Questions about the system or process (e.g., "How does this work?")
#    - Casual conversation (e.g., "Hello!", "How are you?")
#    - Questions unrelated to the database (e.g., "What is the weather today?")
#    - Question about this application itself (e.g., "What is this application? / Tell me about you")

# 2. **SQL Question**: A question that requires generating an SQL query to retrieve data from the database(refer the above table schema). Examples include:
#    - Questions asking for specific data (e.g., "How many customers are there?")
#    - Questions involving filtering, sorting, or aggregating data (e.g., "Show me the top 5 products by sales.")

# Rules:
# - If the question is about retrieving or manipulating data from the database(refer the above table schema), classify it as "SQL Question."
# - If the question is unrelated to data retrieval or is a general conversation, classify it as "General Question."
# - Do not generate any SQL queries or extra text.
# - Do not generate any code, i repeat, dont generate code in any languages
# - Only respond with one of the following: "General Question" or "SQL Question."

# Examples:
# - Input: "What tables are in the database?" → Output: "General Question"
# - Input: "How many customers are there?" → Output: "SQL Question"
# - Input: "Hello, how are you?" → Output: "General Question"
# - Input: "Show me the total sales for 2023." → Output: "SQL Question"

# Now, classify the given question:
# {query}

# """
response_synthesis_template = (
   "This is an Text to SQL Application, developed by Coats Organization."
   "Given an input question, synthesize a response from the query results.\n"
    "Previous Chat History: {chat_history_str}\n"
    "Query: {query_str}\n"
    "SQL: {sql_query}\n"
    "SQL Response: {context_str}\n"
    "Response: "
)
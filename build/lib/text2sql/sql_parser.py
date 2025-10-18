from llama_index.core.llms import ChatMessage, ChatResponse

def parse_response_to_sql(chat_response: ChatResponse | ChatMessage) -> str:

    """Parse response to SQL."""
    response = None
    if isinstance(chat_response, ChatMessage):
        response = chat_response.content
    else:
        response = chat_response.message.content
    sql_query_start = response.find("SQLQuery:")

    if sql_query_start != -1:
        response = response[sql_query_start:]

        if response.startswith("SQLQuery:"):
            response = response[len("SQLQuery:") :]
    sql_result_start = response.find("SQLResult:")

    if sql_result_start != -1:
        response = response[:sql_result_start]
        
    return response.replace("```sql", "").replace("```", "").strip()
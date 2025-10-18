general_response_template = """

This is an Text to SQL Application, developed by Coats Organization! 

Tables listed below and context is also provide below.
{schema}

Previous chat history is given below: 
{chat_history_str}

Given question: {query}

Generate a general response for the above question. Use the above schema and refer to the chat history only if necessary for the question.

Dont generate any code.

Response : 
"""
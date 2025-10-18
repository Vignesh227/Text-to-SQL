from llama_index.core.workflow import Event

print("\n events.py called \n")

# To classify the user question (SQL based Question / General Question)
class ClassifyUserQuestionEvent(Event):
    query : str
    
# Generates response for general questions 
class GeneralResponseEvent(Event):
    query : str
    table_context_str : str
    chat_history_str : str


 # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


# Stores retrieved table schema information
class TableRetrieveEvent(Event):
    table_context_str : str
    query : str
    iteration_number : int

# Stores the generated SQL Query, and generates SQL basesd response
class Text2SQLEvent(Event):
    sql : str
    query : str
    table_context_str : str
    iteration_number : int

class SampleRetriveEvent(Event):
    query : str
    sample_query : str
    table_context_str : str
    iteration_number : int

# Stores information about a failed SQL query execution.
class SQLFailureEvent(Event):
    query : str
    error : str
    sql : str
    table_context_str : str
    iteration_number : int

class SQLCheckEvent(Event):
    query : str
    context : str

class PrepEvent(Event):
    query : str
    iteration_number : int

# Indicates progress in the workflow.
class ProgressEvent(Event):
    result : str

# Streams LLM generated tokens.
class TokenEvent(Event):
    token : str
    
print("\n retriever.py called \n")

from llama_index.core.retrievers import SQLRetriever
from text2sql.utils import sql_database
from text2sql.core.index.handler import table_index, sample_query_index

from llama_index.core.objects import SQLTableSchema
sql_retriever = SQLRetriever(sql_database)

object_retriever = table_index.as_retriever(similarity_top_k = 3)

sample_query_retriever = sample_query_index.as_retriever(similarity_top_k = 3)

print("\n Retriver Called ! ")

def format_nodes_as_table_schema(nodes):
    table_schemas = []
    
    for node in nodes:
        table_name = node.metadata.get("name")
        table_summary = node.metadata.get("context")
        
        schema = SQLTableSchema(table_name = table_name,context_str = table_summary)
        table_schemas.append(schema)

    print("\n format done ! ")
    
    return table_schemas



# if __name__ == '__main__':
# results = object_retriever.aretrieve("List down the materials details of 200X2X12 countply, BPC substrate and G000704 Fibretype")




    # print(object_retriever.retrieve("List down the materials details of 200X2X12 countply, BPC substrate and G000704 Fibretype"), "\n\n\n\n\n NEW : \n\n")
    # print(sample_query_retriever.retrieve("List down the materials details of 200X2X12 countply, BPC substrate and G000704 Fibretype"))





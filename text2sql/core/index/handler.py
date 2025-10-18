# from llama_index.core.objects import ObjectIndex, SQLTableNodeMapping
# from llama_index.core import VectorStoreIndex

print("\n handler.py called \n")

# from text2sql.table_context import table_schema_objs
from text2sql.core.index.setup import chroma_data_indexer as data_indexer
# from text2sql.core.ai_model.models import embed_model
# from text2sql.utils import sql_database

# from text2sql.sample_query import sample_response_nodes 
# table_node_mapping = SQLTableNodeMapping(sql_database)

# from llama_index.core.settings import Settings
# Settings.embed_model = embed_model

print("\n Handler Called ")

table_vector_store = data_indexer.get_vector_store(collection_name = "table_details")
# table_storage_context = data_indexer.get_storage_context(vector_store = table_vector_store)

# table_index = ObjectIndex.from_objects(
#     objects = table_schema_objs,
#     object_mapping=table_node_mapping,
#     index_cls = VectorStoreIndex,
#     storage_context = table_storage_context,
#     index_kwargs={"embed_model": embed_model} 
# )
table_index = data_indexer.load_index(vector_store = table_vector_store)


# try:
#     data_indexer.index_data(
#         collection_name = "Sample_Queries",
#         data = sample_response_nodes
#     )

# except Exception as e:
#     print(f"Error while indexing data: {e}")

sample_query_vector_store = data_indexer.get_vector_store(collection_name = "Sample_Queries")
sample_query_index = data_indexer.load_index(vector_store = sample_query_vector_store)





# if __name__ == "__main__":
#     print(sample_query_index)
#     print(table_context_index)
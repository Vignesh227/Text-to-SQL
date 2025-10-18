
print("\n table_context.py called \n")

from llama_index.core.objects import (
    # SQLTableNodeMapping, 
    # ObjectIndex, 
    SQLTableSchema 
)

from llama_index.core import SQLDatabase
from typing import List

# from text2sql.core.database.setup import db_conn
# from text2sql.config import REQUIRED_TABLES
from text2sql.utils import sql_database


import pandas as pd

#
# LOAD TABLE DESCRIPTIONS 
#                           

# def load_table_descriptions(file_path):
#     # Read the CSV file
#     df = pd.read_csv(file_path)

#     # Convert it into a dictionary
#     table_dict = dict(zip(df['Table Name'], df['Table Description']))

#     return table_dict

# file_path = './new_files/table_desc.csv'
# table_descriptions = load_table_descriptions(file_path)


# #
# # LOAD TABLE METADATA 
# #

# def get_table_metadata(inspector, table_name):
#     table_details = {}
    
#     primary_keys = inspector.get_pk_constraint(table_name)['constrained_columns']
#     foreign_keys = inspector.get_foreign_keys(table_name)
#     foreign_key_details = {fk['constrained_columns'][0]: fk['referred_table'] for fk in foreign_keys}
    
#     columns_info = []
#     for column in inspector.get_columns(table_name):
#         column_detail = {
#             'name': column['name'],
#             'type': str(column['type']),
#             'nullable': column['nullable'],
#             'default': column['default']
#             # 'description': descriptions.get(table_name, {}).get(column['name'], 'N/A')
#         }
#         columns_info.append(column_detail)
    
#     table_details['table_name'] = table_name
#     table_details['primary_key'] = primary_keys
#     table_details['foreign_keys'] = foreign_key_details
#     table_details['columns'] = columns_info

#     return table_details


# #
# # COMBINE ALL TABLE DATA  
# #

# # table_documents = []

# # for table_name in required_tables:
# #     # table_metadata = get_table_metadata(db.inspector, table_name, column_descriptions)
# #     table_metadata = get_table_metadata(db.inspector, table_name)
# #     table = db.metadata.tables[table_name]

# #     with engine.connect() as connection:

# #             result = connection.execute(table.select().limit(5)).fetchall()
# #             print(f"\nLoading rows from table '{table_name}'...")

# #             document_text = f"Table: {table_name}\n"
# #             document_text += f"Table description: {table_descriptions[table_name]}\n"
# #             document_text += f"Primary Key: {table_metadata['primary_key']}\n"
# #             document_text += f"Foreign Keys: {table_metadata['foreign_keys']}\n"
# #             document_text += "Columns:\n"

# #             for col in table_metadata['columns']:
# #                 document_text += f" - {col['name']}: {col['type']}, Nullable: {col['nullable']}, Default: {col['default']}, Description: {col.get('description', 'N/A')}\n"

# #             document_text += "\nSample data(records):\n"

# #             for row in result:
# #                 row_data = {column.name: value for column, value in zip(table.columns, row)}
                
# #                 document_text += str(row_data)
# #                 document_text += "\n"
            
# #             document_text += "\n"
# #             table_documents.append(Document(text=document_text))
# #             print(f"document text : {document_text}")


# # iMPORT Table detials
# import re

# with open('./new_files/table_documents.txt', 'r')  as file:
#     content = file.read()

# tables_split = re.split(r'Table: ', content.strip())[1:]

# print("\n Tables imported and splitted! \n ",tables_split[0])



# table_details_docs = {}

# # table = tables_split[0]
# for table in tables_split:

#     table_name = table[0:table.find("Table description:")-1]

#     table_info = table[table.find("Table description:"):]

#     table_details_docs[table_name] = table_info

# # import json
# # json_formatted = json.dumps(table_details_docs, indent=4)
# # print(json_formatted)
# print("\n Table Converted to dictionary format (suitable for indexing) \n")





# table_infos = [
#     {
#         'table_name' : table_name,
#         'table_summary' : table_summary
#     }
#     for table_name, table_summary in table_details_docs.items()
# ]


# table_schema_objs = [
#     SQLTableSchema(table_name=t['table_name'], context_str=t['table_summary'])
#     for t in table_infos
# ]
# print("\n Table info / table schema objs created! \n")


# print(table_schema_objs)



def get_table_context_str(table_schema_objs: List[SQLTableSchema]) -> str:
    """Get a combined table context string."""
    context_strs = []
    for table_schema_obj in table_schema_objs:
        table_info = sql_database.get_single_table_info(table_schema_obj.table_name)
        
        if table_schema_obj.context_str:
            table_opt_context = " The table summary is: "
            table_opt_context += table_schema_obj.context_str
            table_info += table_opt_context

        context_strs.append(table_info)
    
    return "\n\n".join(context_strs)

print("\n Final \n")
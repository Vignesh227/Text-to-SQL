from llama_index.core.objects import (
    SQLTableNodeMapping, 
    ObjectIndex, 
    SQLTableSchema 
)

from llama_index.core import SQLDatabase
from typing import List

from text2sql.core.database import db_conn
from text2sql.config import REQUIRED_TABLES
from text2sql.utils import sql_database


table_infos = [
    {
        'table_name': table_name,
        'table_summary': f"Schema of table {table_name}"
    }
    for table_name in REQUIRED_TABLES
]

table_schema_objs = [
    SQLTableSchema(table_name=t['table_name'], context_str=t['table_summary'])
    for t in table_infos
]

def get_table_context_str(table_schema_objs: List[SQLTableSchema]) -> str:
    """Get a combined table context string."""
    context_strs = []
    for table_schema_obj in table_schema_objs:
        table_info = sql_database.get_single_table_info(table_schema_obj.table_name)
        
        if table_schema_obj.context_str:
            table_opt_context = " The table description is: "
            table_opt_context += table_schema_obj.context_str
            table_info += table_opt_context

        context_strs.append(table_info)
    
    return "\n\n".join(context_strs)
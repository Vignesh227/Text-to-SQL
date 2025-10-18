from llama_index.core.objects import SQLTableNodeMapping, SQLTableSchema
from llama_index.core import SQLDatabase
from text2sql.core.database import db_conn
from text2sql.config import REQUIRED_TABLES

sql_database = SQLDatabase(db_conn.engine, include_tables = REQUIRED_TABLES)
table_node_mapping = SQLTableNodeMapping(sql_database)

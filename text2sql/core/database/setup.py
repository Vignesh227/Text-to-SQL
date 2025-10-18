from text2sql.core.database.connection import DatabaseConnection
from text2sql.core.database.database_config import database_settings



print("\n database -> Setup.py called")

db_conn = DatabaseConnection(
    server_name = database_settings.server_name,
    database_name = database_settings.database_name,
    user = database_settings.user,
    password = database_settings.password,
    driver_name = database_settings.driver_name,
    port = database_settings.port,
    required_tables = None
)

# if __name__ == "__main__":
#     print(db_conn.connection_url)
#     print(db_conn.engine)

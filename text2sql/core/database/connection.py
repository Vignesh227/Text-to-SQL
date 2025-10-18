from sqlalchemy import URL, Engine
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.exc import InterfaceError, OperationalError
from typing import List, Union, Optional

from text2sql.core.database.database_config import database_settings
from text2sql.config import REQUIRED_TABLES

print("\n Connection.py called \n")

class DatabaseConnection:
    def __init__(
        self,     
        server_name : str, 
        database_name : str, 
        user : str, 
        password : str, 
        driver_name : str, 
        port : int, 
        required_tables : Optional[List[int]] = None
    ):
        
        self.server_name = server_name
        self.database_name = database_name
        self.user = user
        self.password = password
        self.driver_name = driver_name
        self.port = port
        self.requried_tables = required_tables
        self._connection_url = None
        self._engine = None
        self._inspector = None
        self._metadata = None

    @property
    def connection_url(self) -> Optional[str]:
        try:
            if self._connection_url is None:
                odbc_string = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={self.server_name};DATABASE={self.database_name};UID={self.user};PWD={self.password}"
                connection_string = URL.create(
                    "mssql+pyodbc", 
                    query={"odbc_connect": odbc_string})
                self._connection_url = connection_string

        except Exception as e:
            print("Please check the connection parameters")

        return self._connection_url 

    @property
    def engine(self) -> Optional[Engine]:
        try: 
            if self._engine is None:
                self._engine = create_engine(self.connection_url)
        except Exception as e:
            print("Please check the connection parameters")

        return self._engine
    
    @property
    def inspector(self) -> Optional[Inspector]:
        try:
            if self._inspector is None:
                self._inspector = inspect(self.engine)
        except Exception as e:
            print("Please check the connection parameters")

        return self._inspector
    
    @property
    def metadata(self):
        _metadata = MetaData()

        try:
            if self._metadata is None:
                self._metadata = _metadata.reflect(bind = self.engine, only = self.requried_tables)
            else:
               self._metadata = _metadata.reflect(bind = self.engine)

        except InterfaceError as e:
            print(f"{e} : Please check the connection string/parameters")
        except OperationalError as e:
            print(f"{e} : SQL server is not reachable, please check the connection")
        except Exception as e:
            print(f"{e} : Error with establishing connection to the database")

        return self._metadata
    
# if __name__ == '__main__':

#     connection = DatabaseConnection(
#         server_name = database_settings.server_name,
#         database_name = database_settings.database_name,
#         user = database_settings.user,
#         password = database_settings.password,
#         driver_name = database_settings.driver_name,
#         port = database_settings.port,
#         required_tables = REQUIRED_TABLES
#     )

#     print(connection.connection_url)
#     print(connection.engine)
   
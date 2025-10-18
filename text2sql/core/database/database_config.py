from pydantic import (
    BaseModel,
    Field,
    
)

print("\n Database config.py called \n")

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Union, Optional

class DatabaseConnectionConfig(BaseSettings):
    server_name : str
    database_name :str
    user : str
    password : str
    driver_name : str
    port : int

    model_config = SettingsConfigDict(
        env_file = ".env",
        extra = "ignore"
    )

database_settings = DatabaseConnectionConfig()


# if __name__ == "__main__":
#     settings = DatabaseConnectionConfig()
#     print(settings)
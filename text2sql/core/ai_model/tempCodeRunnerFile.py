from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Union

class AIConfig(BaseSettings):
    llm_model_name : str 
    embed_model_name : str
    temperature : float
    max_tokens : int
    top_p : float

    model_config = SettingsConfigDict(
        env_file=".env",
        extra = "ignore",
    )

model_settings = AIConfig()

if __name__ == "__main__":
    settings = AIConfig()
    # print(AIConfig.llm_model_name)
    print(settings)
    

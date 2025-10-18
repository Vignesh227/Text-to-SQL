from llama_index.llms.vertex import Vertex
from llama_index.embeddings.vertex import VertexTextEmbedding
from google.oauth2 import service_account

from text2sql.core.ai_model.model_config import model_settings

import os

# from llama_index.core.settings import Settings

print("\n models.py called \n")


# filename = "C:/Vignesh/Text2Sql/service_account 1 1.json"
filename = os.path.join(os.getcwd(), "service_account 1 1.json")
credentials = ( 
    service_account.Credentials.from_service_account_file(filename)
)


llm = Vertex(
    model = model_settings.llm_model_name,
    temperature = model_settings.temperature,
    credentials=credentials,
    project = credentials.project_id,
    max_tokens = model_settings.max_tokens
)

embed_model = VertexTextEmbedding(
    model_name = model_settings.embed_model_name,
    credentials=credentials,
    project = credentials.project_id,
)


# Settings.embed_model = embed_model 

if __name__ == "__main__":
    print(embed_model)



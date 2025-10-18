from text2sql.core.index.chroma_indexer import ChromaDataIndexer
from text2sql.core.ai_model.models import embed_model
from text2sql.config import CHROMA_PATH

print("\n index -> setup.py called \n")

chroma_data_indexer = ChromaDataIndexer(
    embed_model = embed_model,
    path = CHROMA_PATH
)

chroma_data_indexer.initialize_chroma_client()

# if __name__ == "__main__":
#     print(chroma_data_indexer.is_chroma_client_active)
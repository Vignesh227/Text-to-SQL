print("\n chroma_indexer.py called \n")

from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import VectorStoreIndex
from text2sql.core.index.base_indexer import BaseDataIndexer
import chromadb

from text2sql.core.ai_model.models import embed_model

class ChromaDataIndexer(BaseDataIndexer):
    def __init__(
            self, 
            embed_model , 
            path : str,
        ):

        super().__init__(embed_model)
        self.path = path
        self.is_chroma_client_active= False
        self.embed_model = embed_model
        self.chroma_client = None
        self.initialize_chroma_client()

    def initialize_chroma_client(self):
        if not self.is_chroma_client_active:
            self.is_chroma_client_active = True
        else:
            print("Chroma Client is active")
        self.chroma_client = chromadb.PersistentClient(self.path)

    def list_all_collections(self):
        return self.chroma_client.list_collections()
    
    def _create_collection(self, collection_name):
        return self.chroma_client.create_collection(collection_name)
    
    def get_collection(self, collection_name):
        try:
            return self.chroma_client.get_collection(collection_name)
        except Exception as e:
            raise LookupError(f"Collection '{collection_name}' not found: {e}")
    
    def get_vector_store(self, collection_name):
        collections = self.list_all_collections()
        # collection_name = collection.name
        collection_exists = any(collection.name == collection_name for collection in collections)

        if not collection_exists:
            collection = self._create_collection(collection_name)
        else:
            collection = self.get_collection(collection_name)

        vector_store = ChromaVectorStore(chroma_collection = collection)
        return vector_store
    
    def load_index(self, vector_store):
        self.storage_context = self.get_storage_context(vector_store)

        index = VectorStoreIndex.from_vector_store(
            vector_store = vector_store,
            storage_context = self.storage_context,
            embed_model = self.embed_model
        )

        return index
    
    def index_data(self, collection_name, data):
        vector_store = self.get_vector_store(collection_name)

        index = self.load_index(vector_store = vector_store)
        print(index, "wefwef")
        for nodes in data:
            print("1")
            index.insert(nodes)

# if __name__ == "__main__":
#     from text2sql.config import CHROMA_PATH
#     chroma_data_indexer = ChromaDataIndexer(
#         embed_model = embed_model,
#         path = CHROMA_PATH
#     )
#     print(chroma_data_indexer.is_chroma_client_active)
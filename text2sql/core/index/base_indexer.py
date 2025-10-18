print("\n base indexer.py callled")

from llama_index.core import StorageContext
from abc import ABC, abstractmethod
import chromadb

class BaseDataIndexer(ABC):
    def __init__(self, embed_model):
        self.embed_model = embed_model
        self.storage_context = None
    
    @abstractmethod
    def load_index(self):
        pass
    
    @abstractmethod
    def index_data(self, data):
        pass

    def get_storage_context(self, vector_store):
        self.storage_context = StorageContext.from_defaults(vector_store = vector_store)
        return self.storage_context



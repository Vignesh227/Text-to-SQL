# Exe
# Exe

from abc import ABC, abstractmethod


# Exe
from IPython.display import Markdown, display
from llama_index.core import Document, load_index_from_storage, PromptTemplate, Settings, SQLDatabase, StorageContext, VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.llms import ChatResponse
from llama_index.core.objects import SQLTableNodeMapping, ObjectIndex, SQLTableSchema 
from llama_index.core.prompts.default_prompts import DEFAULT_TEXT_TO_SQL_PROMPT
from llama_index.core.query_pipeline import CustomQueryComponent, FnComponent, InputComponent, Link, QueryPipeline as QP
from llama_index.core.retrievers import SQLRetriever, VectorIndexRetriever
from llama_index.core.schema import TextNode
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.llms.vertex import Vertex
from llama_index.embeddings.vertex import VertexTextEmbedding
from llama_index.llms.gemini import Gemini
from llama_index.vector_stores.chroma import ChromaVectorStore
from google.oauth2 import service_account
from pathlib import Path
# from pyvis.network import Network
from sqlalchemy import Column, create_engine, Date, ForeignKey, inspect, Integer, LargeBinary, MetaData, Numeric, SmallInteger, String, Table, Text
from typing import Dict, List
import chromadb
import getpass
import google.generativeai as genai
import os
import pandas as pd
import nest_asyncio
nest_asyncio.apply()


# Exe
filename = "service_account 1 1.json"

credentials = (
    service_account.Credentials.from_service_account_file(filename)
)

llm = Vertex(
    model ="gemini-1.5-pro-002", 
    # safety_settings=safety_settings, 
    project=credentials.project_id, 
    credentials=credentials,
    temperature = 0.1,
    max_tokens = 8192
)
# llm = LangChainLLM(llm = model)


embed_model = VertexTextEmbedding(
    model_name="text-embedding-004" ,
    project=credentials.project_id, 
    credentials=credentials, 
    # location="us-central1"
)

Settings.llm = llm
Settings.embed_model = embed_model


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

class ChromaDataIndexer(BaseDataIndexer):
    def __init__(
            self, 
            embed_model, 
            path,
        ):

        super().__init__(embed_model)
        self.path = path
        self.is_chroma_client_active= False
        self.embed_model = embed_model
        self.chroma_client = None

    def initialize_chroma_client(self):
        # print("Prem nit")
        
        if not self.is_chroma_client_active:
            self.chroma_client = chromadb.PersistentClient(self.path)
            self.is_chroma_client_active = True
        else:
            print("Chroma Client is already active")
        
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
        

        # collection_names = [self.chroma_client.get_collection(name=name, embedding_function=self.embed_model) for name in collections ]

        collection_exists = any(collection.name == collection_name for collection in collections)

        # if collection_name in collection_names:
        #     collection_exixts = True

        if not collection_exists:
            collection = self._create_collection(collection_name)
            print("\n Collection created  successfully")
        else:
            collection = self.get_collection(collection_name)
            print("\n Collection fetched  successfully")

        print(collection)

        vector_store = ChromaVectorStore(chroma_collection = collection)

        
        return vector_store
    
    def load_index(self, vector_store):
        self.storage_context = self.get_storage_context(vector_store)

        index = VectorStoreIndex.from_vector_store(
            vector_store = vector_store,
            storage_context = self.storage_context,
            embed_model = self.embed_model
        )
        print("\n Vector loaded successfully")
        return index
    
    def index_data(self, collection_name, data):
        vector_store = self.get_vector_store(collection_name)

        index = self.load_index(vector_store = vector_store)
        
        for nodes in data:
            index.insert(nodes)

        print("\n Data indexed successfully")

data_indexer = ChromaDataIndexer(
    embed_model = embed_model, 
    path = "/new_db",
)



print(data_indexer.list_all_collections())



vector_store = data_indexer.get_vector_store(collection_name = "table_details")
storage_context = data_indexer.get_storage_context(vector_store)

table_index = data_indexer.load_index(vector_store=vector_store)
table_retriever = table_index.as_retriever(similarity_top_k = 5)

table_obj_retriever.retrieve("List down the materials details of 200X2X12 countply, BPC substrate and G000704 Fibretype")

print(table_obj_retriever)
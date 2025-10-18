from llama_index.core.memory import ChatMemoryBuffer # To maintain converstion history
from llama_index.core.llms import ChatMessage
import json
import os

print("\n chat_history.py called \n")

# Directory to save chat history
CHAT_HISTORY_DIR = "chat_history"

# Ensure the directory exists
os.makedirs(CHAT_HISTORY_DIR, exist_ok=True)


# Generate the file path for a given user's chat history.
def get_chat_history_filepath(user_id: str) -> str:
    return os.path.join(CHAT_HISTORY_DIR, f"uID_{user_id}_chat_history.json")




# Save the chat history to a JSON file.
def save_chat_history(user_id: str, memory: ChatMemoryBuffer) -> None:
    
    chat_history = memory.get()  # Get chat messages from memory

    serialized_history = [
        {"role": msg.role, "content": msg.content} for msg in chat_history
    ]

    # Load the file
    file_path = get_chat_history_filepath(user_id) 

    # Save the messages into the file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(serialized_history, f, ensure_ascii=False, indent=4)

    print(f"Chat history saved for the user : {user_id}.")




# Load chat history from a JSON file into a ChatMemoryBuffer
def load_chat_history(user_id: str, llm) -> ChatMemoryBuffer:
    
    file_path = get_chat_history_filepath(user_id)
    memory = ChatMemoryBuffer.from_defaults(llm=llm)
    
    # Load the existing chat data into the memory (if data exists)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            serialized_history = json.load(f)
            for msg in serialized_history:
                memory.put(ChatMessage(role=msg["role"], content=msg["content"]))
        print(f"Chat history loaded for user : {user_id}.")

    else:
        print(f"No chat history found for user : {user_id}.")
    
    return memory

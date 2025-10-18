
print("\n sample_query.py called \n")


from llama_index.core import Document

documents = []

with open("./new_files/sample qry.txt", "r", encoding="utf-8") as file:
    content = file.read().strip()

# Splitting based on "Question:" to get individual question blocks
entries = content.split("Question:")

for entry in entries[1:]:  # Skipping the first empty entry
    parts = entry.split("Answer:")
    if len(parts) == 2:
        question = parts[0].strip()
        sql_query = parts[1].strip()
        document_text = "Question:\n" + question + "\nSqlquery:\n" + sql_query
        documents.append({'text' : document_text})

# print(documents)
# Printing extracted data
# for doc in documents:
    # print(doc)


sample_response_nodes = [Document(text = doc["text"]) for doc in documents]


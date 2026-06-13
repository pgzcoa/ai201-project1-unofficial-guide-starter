import os
import re
import random

# 1. Load Documents

def load_documents(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith("txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            documents.append({
                "id": filename.replace(".txt", ""),
                "text": text
            })
    return documents

#2. Clean Texts
    
def clean_text(text):
    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    #Replace HTML entities
    text = text.replace("&nbsp;", "", ).replace("&amp;", "&")

    #Remove repeated whitespace
    text = re.sub(r"\s+", "", text)

    return text.strip()

#3. Chunking

def chunk_text(text, chunk_size=50, overlap=10):
    tokens = text.split()
    chunks = []
    start = 0

    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start::end]

        if chunk_tokens:
            chunks.append(" ".join(chunk_tokens))

        start += chunk_size - overlap

    return chunks

    # Main Pipeline Execution

if __name__ == "__main__": 
    print("Loading documents...")
    docs = load_documents("data/raw/")

    print(f"Loaded {len(docs)} documents.")

    #Clean documents
    cleaned_docs = []
    for doc  in docs:
        cleaned_docs.append({
            "id": doc["id"],
            "text": clean_text(doc["text"])
        })

#4. Chunking documents

all_chunks = []
for doc in cleaned_docs:
    chunks = chunk_text(doc["text"], chunk_size=50, overlap=10)
    for i, chunk in enumerate(chunks):
        all_chunks.append({
            "doc_id": doc["id"],
            "chunk_id": f"{doc['id']}_{i}",
            "text": chunk 
        })

    print("Total chunks created:", len(all_chunks))

    #Print 5 random chunks for inspection

    print("\n-----SAMPLE CHUNKS-----")
    for c in random.sample(all_chunks, min(5, len(all_chunks))):
        print("\nChunk:", c["chunk_id"])
        print(c["text"])





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
    text = re.sub(r"\s+", " ", text)

    return text.strip()

#3. Chunking

def chunk_text(text, chunk_size=50, overlap=10):
    tokens = text.split()
    chunks = []
    start = 0

    while start < len(tokens):
        end = start + chunk_size
        chunk_tokens = tokens[start:end]

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

    documents = cleaned_docs

#4. Chunking documents

all_chunks = []
chunk_id = 1

for doc in documents:
    text = doc["text"]
    doc_chunks = chunk_text(text, chunk_size=50, overlap=10)

    for chunk in doc_chunks:
        all_chunks.append({
            "chunk_id": chunk_id,
            "text": chunk 
        })
        chunk_id += 1


    #Print 5 random chunks for inspection

print("Total chunks created:", len(all_chunks))

print("\n-----SAMPLE CHUNKS-----")
for c in random.sample(all_chunks, min(5, len(all_chunks))):
    print("\nChunk:", c["chunk_id"])
    print(c["text"])

    #Embedding + Chromadb

from sentence_transformers import SentenceTransformer 
import chromadb 
from chromadb.config import Settings
import uuid

print("\nLoading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+paraquet",
    persist_directory="vectorstore"
))

collection = chroma_client.get_or_create_collection(
    name="course_chunks",
    metadata={"hnsw:space": "cosine"}
)

#Emded and store chunks

def embed_and_store(chunks):
    texts = [c["text"] for c in chunks]
    metadatas =  [c["text"] for c in chunks]
    ids = [str(uuid.uuid4()) for _ in chunks]

    embeddings = model.encode(texts, show_progress_bar=True)

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas
    )

    print(f"\nStored {len(chunks)} chunks in ChromaDB.")

embed_and_store(all_chunks)

#Retrieval function

def retrieve(query, k=4):
    query_embedding = model.encode([query])[0]

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k 
    )

    formatted = []
    for doc, meta, dist in zip(results["documents"][0],
                               results["metadatas"][0],
                               results["distances"][0]):

        formatted.append({
            "text": doc,
            "source": meta["source"],
            "position": meta["position"],
            "distance": dist
        })

    return formatted

#Debug print helper

def print_results(results):
    for r in results:
        print("\n---Retrieved Chunk---")
        print(f"Source: {r['source']} | Position: {r['position']}| Distance: {r['distance']:.4f}")
        print(r["text"])
        print("---------------")

#Test retrieval

print("\nTesting retrieval...")
test_query = "What are the best pizza spots in southern California?"
results = retrieve(test_query, k=5)
print_results(results)



 
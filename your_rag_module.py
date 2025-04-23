from llama_cpp import Llama
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path

# --- Configuration ---
MODEL_PATH = "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
VECTOR_INDEX_PATH = "vectorstore/ctse_faiss.index"
CHUNKS_PATH = "vectorstore/chunks.txt"
TOP_K = 3

# Load model once
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=6, n_gpu_layers=20)

# Load vector store
index = faiss.read_index(VECTOR_INDEX_PATH)
with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
    chunks = f.read().split("\n\n")

# Sentence embedding model
embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def retrieve_chunks(query, k=TOP_K):
    query_vec = embedder.encode([query])
    D, I = index.search(np.array(query_vec).astype("float32"), k)
    return [chunks[i] for i in I[0]]

def generate_answer(query):
    context_chunks = retrieve_chunks(query)
    context = "\n---\n".join(context_chunks)

    prompt = f"""
You are an expert assistant helping students learn about Current Trends in Software Engineering (CTSE).
Use the following context to answer the question.

Context:
{context}

Question: {query}
Answer:
"""
    response = llm(prompt, max_tokens=512, stop=["\n\n"])
    return response["choices"][0]["text"].strip(), context_chunks

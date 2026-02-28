#!/usr/bin/env python3
"""ChromaDB semantic search server for Syncrescendence vault."""
from config import *

import os
import hashlib
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import chromadb
from sentence_transformers import SentenceTransformer
import uvicorn

VAULT = Path("/Users/home/Desktop/syncrescendence")
CHROMA_DIR = Path("/Users/home/.syncrescendence/chroma")
CHROMA_DIR.mkdir(parents=True, exist_ok=True)

COLLECTIONS_MAP = {
    "canon": VAULT / "canon",
    "engine": VAULT / "engine",
    "sigma": VAULT / "praxis",
}

app = FastAPI(title="Syncrescendence ChromaDB Server")
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path=str(CHROMA_DIR))


class SearchRequest(BaseModel):
    query: str
    collection: str = "canon"
    top_k: int = 5


class IndexRequest(BaseModel):
    path: str
    collection: str = "canon"


def chunk_text(text: str, size: int = 500) -> list[str]:
    """Split text into roughly equal chunks at paragraph boundaries."""
    paragraphs = text.split("\n\n")
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) > size and current:
            chunks.append(current.strip())
            current = para
        else:
            current = current + "\n\n" + para if current else para
    if current.strip():
        chunks.append(current.strip())
    return chunks if chunks else [text[:size]]


def index_file(filepath: Path, collection_name: str) -> int:
    """Index a single markdown file into a chromadb collection."""
    col = client.get_or_create_collection(name=collection_name)
    text = filepath.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        return 0
    chunks = chunk_text(text)
    ids, docs, embeddings, metadatas = [], [], [], []
    for i, chunk in enumerate(chunks):
        chunk_id = hashlib.md5(f"{filepath}:{i}".encode()).hexdigest()
        embedding = model.encode(chunk).tolist()
        ids.append(chunk_id)
        docs.append(chunk)
        embeddings.append(embedding)
        metadatas.append({"source": str(filepath), "chunk": i})
    col.upsert(ids=ids, documents=docs, embeddings=embeddings, metadatas=metadatas)
    return len(chunks)


@app.get("/health")
def health():
    collections = [c.name for c in client.list_collections()]
    return {"status": "ok", "collections": collections, "chroma_dir": str(CHROMA_DIR)}


@app.post("/search")
def search(req: SearchRequest):
    try:
        col = client.get_collection(name=req.collection)
    except Exception:
        raise HTTPException(404, f"Collection '{req.collection}' not found. Index first.")
    query_embedding = model.encode(req.query).tolist()
    results = col.query(query_embeddings=[query_embedding], n_results=req.top_k)
    return {
        "query": req.query,
        "collection": req.collection,
        "results": [
            {"document": doc, "metadata": meta, "distance": dist}
            for doc, meta, dist in zip(
                results["documents"][0],
                results["metadatas"][0],
                results["distances"][0],
            )
        ],
    }


@app.post("/index")
def index(req: IndexRequest):
    target = Path(req.path) if os.path.isabs(req.path) else VAULT / req.path
    if not target.exists():
        raise HTTPException(404, f"Path not found: {target}")
    total = 0
    if target.is_file() and target.suffix == ".md":
        total = index_file(target, req.collection)
    elif target.is_dir():
        for md in sorted(target.rglob("*.md")):
            total += index_file(md, req.collection)
    else:
        raise HTTPException(400, "Path must be a .md file or directory")
    return {"indexed_chunks": total, "collection": req.collection, "path": str(target)}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8765, log_level="info")

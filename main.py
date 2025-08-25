import os
import redis
from fastapi import FastAPI
from pydantic import BaseModel
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams
from sentence_transformers import SentenceTransformer
import uuid

from app.core.routers import router as core_router

from app.user.routers import router as user_router
from app.job.routers import router as job_router

app = FastAPI(
    title="SimpleAPI",
    description="A simple FastAPI application with core and subscription functionality.",
    version="1.0.0",
)

app.include_router(core_router, prefix="/core", tags=["Core"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(job_router, prefix="/job", tags=["Job"])

# Redis configuration
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.get("/redis-test")
async def redis_test():
    try:
        redis_client.ping()
        return {"message": "Redis connection successful!"}
    except redis.exceptions.ConnectionError as e:
        return {"message": f"Redis connection failed: {e}"}

# Qdrant configuration
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", 6333))

qdrant = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

# Initialize embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create collection (only once)
collection_name = "documents"
qdrant.recreate_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=384, distance="Cosine")
)

# Input schema
class Document(BaseModel):
    text: str

@app.post("/insert")
def insert_document(doc: Document):
    vector = model.encode(doc.text).tolist()
    point = PointStruct(id=str(uuid.uuid4()), vector=vector, payload={"text": doc.text})
    qdrant.upsert(collection_name=collection_name, points=[point])
    return {"status": "inserted", "text": doc.text}

@app.get("/search")
def search(query: str, limit: int = 3):
    query_vector = model.encode(query).tolist()
    results = qdrant.search(collection_name=collection_name, query_vector=query_vector, limit=limit)
    return [{"id": r.id, "score": r.score, "text": r.payload["text"]} for r in results]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import APIRouter
from fastapi import APIRouter
from pydantic import BaseModel
from qdrant_client.models import PointStruct, VectorParams
import uuid
from app.config.config import qdrant_client, model
from .services import CoreService

router = APIRouter()
service = CoreService()

class Document(BaseModel):
    text: str

@router.get("/health", operation_id="health_check")
async def health_check():
    return await service.health_check()

@router.get("/info", operation_id="get_app_info")
async def get_app_info():
    return await service.get_app_info()

@router.post("/insert")
def insert(doc: Document):
    collection_name = "documents"
    qdrant_client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=model.get_sentence_embedding_dimension(), distance="Cosine")
    )
    vector = model.encode(doc.text).tolist()
    point = PointStruct(id=str(uuid.uuid4()), vector=vector, payload={"text": doc.text})
    qdrant_client.upsert(collection_name=collection_name, points=[point])
    return {"status": "inserted", "text": doc.text}

@router.get("/search")
def search(query: str, limit: int = 3):
    collection_name = "documents"
    query_vector = model.encode(query).tolist()
    results = qdrant_client.search(collection_name=collection_name, query_vector=query_vector, limit=limit)
    return [{"id": r.id, "score": r.score, "text": r.payload["text"]} for r in results]
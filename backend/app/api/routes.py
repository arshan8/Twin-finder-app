from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.face import get_face_embedding
from app.services.qdrant import find_similar_face
from app.models.schemas import TwinResult

router = APIRouter()

@router.post("/find_twin", response_model=TwinResult)
async def find_twin(file: UploadFile = File(...)):
    # Read image bytes
    image_bytes = await file.read()
    # Get face embedding
    embedding = get_face_embedding(image_bytes)
    if embedding is None:
        raise HTTPException(status_code=400, detail="No face detected in the image.")
    # Query Qdrant for the most similar face
    result = find_similar_face(embedding)
    if result is None:
        raise HTTPException(status_code=404, detail="No similar face found.")
    return result
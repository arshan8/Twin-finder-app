from vector_twin.qdrant import get_qdrant_client

def find_similar_face(embedding, collection_name="celebrities"):
    client = get_qdrant_client()
    # Ensure embedding is a list of floats
    embedding = embedding.flatten().tolist() if hasattr(embedding, "flatten") else list(embedding)
    search_result = client.search(
        collection_name=collection_name,
        query_vector=embedding,
        limit=1,
        with_payload=True
    )
    if not search_result:
        return None
    hit = search_result[0]
    payload = hit.payload
    return {
        "label": payload.get("label", ""),
        "similarity": hit.score,
        "image_base64": payload.get("image_data", "")
    }
import os
import sys
import uuid
import base64
from io import BytesIO

# Ensure vector_twin is importable
src_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if src_path not in sys.path:
    sys.path.append(src_path)

from datasets import load_dataset
from tqdm import tqdm
from PIL import Image
import numpy as np
from vector_twin.models import initialize_models, process_single_image
from vector_twin.qdrant import get_qdrant_client, create_collection

def insert_image_embedding(qdrant_client, embedding, image_base64, point_id, label):
    """Insert image embedding into Qdrant with proper error handling"""
    try:
        embedding_list = embedding.flatten().tolist() if isinstance(embedding, np.ndarray) else list(embedding)
        point = {
            "id": point_id,
            "vector": embedding_list,
            "payload": {
                "label": str(label),
                "image_data": image_base64,
                "has_image": True
            }
        }
        result = qdrant_client.upsert(
            collection_name="celebrities",
            points=[point]
        )
        return result
    except Exception as e:
        print(f"Error inserting embedding: {str(e)}")
        raise e

def compress_image(image, max_size=(512, 512), quality=85):
    """Compress image to reduce base64 size"""
    if image.mode != 'RGB':
        image = image.convert('RGB')
    if image.size[0] > max_size[0] or image.size[1] > max_size[1]:
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
    buffered = BytesIO()
    image.save(buffered, format="JPEG", quality=quality, optimize=True)
    return buffered.getvalue()

def main():
    try:
        print("Connecting to Qdrant...")
        qdrant_client = get_qdrant_client()

        collection_name = "celebrities"
        collections = qdrant_client.get_collections().collections
        collection_names = [c.name for c in collections]
        if collection_name in collection_names:
            count = qdrant_client.count(collection_name=collection_name, exact=True).count
            if count > 0:
                print(f"[INFO] Collection '{collection_name}' already has {count} points. Skipping embedding generation.")
                return

        print("Setting up collection...")
        try:
            create_collection(qdrant_client)
            print("Collection 'celebrities' created successfully")
        except Exception as e:
            if "already exists" in str(e).lower():
                print("Collection 'celebrities' already exists")
            else:
                print(f"Error creating collection: {e}")
                raise e

        print("Loading dataset...")
        dataset = load_dataset("lansinuote/simple_facenet", split="train")
        dataset = dataset.shuffle(seed=42).select(range(120))
        print(f"Loaded {len(dataset)} samples")

        print("Initializing models...")
        # Force CPU usage
        device, mtcnn, resnet = initialize_models()
        print(f"Models initialized on device: {device}")

        print("Generating embeddings...")
        successful_inserts = 0
        failed_inserts = 0

        for idx, row in enumerate(tqdm(dataset, desc="Processing images")):
            try:
                img_embedding = process_single_image(row["image"], device, mtcnn, resnet)
                if img_embedding is None:
                    print(f"No face detected in image {idx}, skipping...")
                    failed_inserts += 1
                    continue

                compressed_image_data = compress_image(row["image"])
                if len(compressed_image_data) > 1024 * 1024:
                    print(f"Image {idx} still too large after compression ({len(compressed_image_data)} bytes), skipping...")
                    failed_inserts += 1
                    continue

                image_base64 = base64.b64encode(compressed_image_data).decode("utf-8")
                point_id = str(uuid.uuid4())

                insert_image_embedding(
                    qdrant_client,
                    img_embedding,
                    image_base64,
                    point_id,
                    row['label']
                )
                successful_inserts += 1

            except Exception as e:
                print(f"Error processing image {idx}: {str(e)}")
                failed_inserts += 1
                continue

        print(f"\nProcessing complete!")
        print(f"Successful inserts: {successful_inserts}")
        print(f"Failed inserts: {failed_inserts}")
        print(f"Total processed: {successful_inserts + failed_inserts}")

        try:
            collection_info = qdrant_client.get_collection("celebrities")
            print(f"Collection now contains {collection_info.points_count} points")
        except Exception as e:
            print(f"Could not get collection info: {e}")

    except Exception as e:
        print(f"Fatal error in main: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

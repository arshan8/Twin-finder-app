from PIL import Image
from io import BytesIO
from vector_twin.models import initialize_models, process_single_image

device, mtcnn, resnet = initialize_models()

def get_face_embedding(image_bytes: bytes):
    image = Image.open(BytesIO(image_bytes))
    embedding = process_single_image(image, device, mtcnn, resnet)
    return embedding
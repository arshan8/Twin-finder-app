from pydantic import BaseModel

class TwinResult(BaseModel):
    label: str
    similarity: float
    image_base64: str
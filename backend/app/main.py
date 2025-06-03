from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Face Twin Finder API",
    description="Find your celebrity twin using face embeddings and Qdrant.",
    version="1.0.0"
)

app.include_router(router)
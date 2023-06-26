from sentence_transformers import SentenceTransformer

from engine.services.model_service import ModelService
from engine.services.vector_db_service import VectorDBService


class EmbeddingService:
    def __init__(self, vector_db_service: VectorDBService, model_service: ModelService):
        self.vector_db_service = vector_db_service
        self.model_service = model_service
        self.model = self.model_service.get_model()

    def get_embeddings(self, texts):
        embeddings = self.model.encode(texts)
        return embeddings


from sentence_transformers import SentenceTransformer

from engine.configs.common import ModelSettings
import logging.config

logger = logging.getLogger(__name__)


class ModelService:
    def __init__(self, config: dict):
        self.config = ModelSettings(**config)
        self.pretrained_model_name = self.config.pretrained_model_name
        self.model = None

    def load_model(self) -> None:
        logger.info(f"Loading model {self.pretrained_model_name}...")
        self.model = SentenceTransformer(self.pretrained_model_name)
        logger.info(f"Loaded model {self.pretrained_model_name}")

    def get_model(self) -> SentenceTransformer:
        return self.model

    def update(self, pretrained_model_name: str) -> SentenceTransformer:
        self.model = SentenceTransformer(pretrained_model_name)
        return self.model

    def delete(self) -> None:
        self.model = None

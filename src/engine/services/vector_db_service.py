from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance

from engine.configs.common import QDrantSettings
from engine.schemas.schemas import Payload
import logging.config


logger = logging.getLogger(__name__)


class VectorDBService:
    def __init__(self, config: dict):
        self.config = QDrantSettings(**config)
        self.client = QdrantClient(host=self.config.host, port=self.config.port)
        self.collection = self.config.collection
        self.embedding_size = self.config.embedding_size

    def init_db(self):
        logger.info("Initializing DB service")
        try:
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(
                    size=self.embedding_size,
                    distance=Distance.COSINE
                )
            )
        except Exception as e:
            if "already exists" in str(e):
                logger.warning(f"Collection {self.collection} already exists")
            else:
                logger.error(f"Error while creating collection {self.collection}: {e}")

    def insert(self, payloads: list[Payload]):
        points = [
            PointStruct(
                id=payload.id,
                vector=payload.vector,
                payload=payload.payload
            )
            for payload in payloads
        ]
        self.client.upsert(
            collection_name=self.collection,
            points=points
        )
        logger.info(f"Inserted {len(points)} points into collection {self.collection}")

    def search(self, query_embeddings, limit: int = 5, skip: int = 0):
        search_result = self.client.search(
            collection_name=self.collection,
            query_vector=query_embeddings,
            limit=limit,
            offset=skip
        )
        return search_result

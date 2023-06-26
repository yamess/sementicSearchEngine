from dependency_injector import containers, providers

from engine.configs.common import GlobalSettings, ModelSettings, QDrantSettings, AppSettings, BlobSettings
from engine.services.embedding_service import EmbeddingService
from engine.services.model_service import ModelService
from engine.services.vector_db_service import VectorDBService
import logging

logger = logging.getLogger(__name__)


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=['engine'])

    config = providers.Configuration(
        pydantic_settings=[
            GlobalSettings(
                app=AppSettings(),
                model=ModelSettings(),
                qdrant=QDrantSettings(),
                blob=BlobSettings()
            )
        ]
    )

    vector_db_service = providers.Singleton(
        VectorDBService,
        config=config.qdrant
    )

    model_service = providers.Singleton(
        ModelService,
        config=config.model
    )

    embedding_service = providers.Factory(
        EmbeddingService,
        vector_db_service=vector_db_service,
        model_service=model_service
    )


def set_dependencies(config: GlobalSettings):
    logger.info("Setting dependencies injection")
    container = Container()
    container.wire(packages=[Container.wiring_config])

    db_service = container.vector_db_service()
    db_service.init_db()

    model_service = container.model_service()
    model_service.load_model()

    return container

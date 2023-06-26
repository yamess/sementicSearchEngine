from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from engine.configs.common import GlobalSettings, AppSettings, ModelSettings, QDrantSettings, BlobSettings
from engine.dependencies.containers import set_dependencies
from engine.routes import base
import logging
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = GlobalSettings(
        app=AppSettings(),
        model=ModelSettings(),
        qdrant=QDrantSettings(),
        blob=BlobSettings()
    )
    container = set_dependencies(config=settings)
    app.container = container
    yield
    logger.info("Application shutdown")


def create_app():
    app_settings = AppSettings()
    application = FastAPI(
        title="Semantic Search Engine Service",
        description="""This is search engine project for text documents, 
                    images and audio , with auto docs for the API and everything""",
        version="0.1.0",
        debug=app_settings.debug,
        docs_url="/docs",
        lifespan=lifespan
    )

    application.include_router(base.route)

    application.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    logger.info("Application configured")
    return application


app = create_app()

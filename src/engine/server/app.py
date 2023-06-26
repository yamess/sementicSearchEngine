from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from engine.configs.common import GlobalSettings, AppSettings, ModelSettings, QDrantSettings, BlobSettings
from engine.routes import base


def create_app():
    settings = GlobalSettings(
        app=AppSettings(),
        model=ModelSettings(),
        qdrant=QDrantSettings(),
        blob=BlobSettings()
    )
    application = FastAPI(
        title="Semantic Search Engine Service",
        description="""This is search engine project for text documents, 
                    images and audio , with auto docs for the API and everything""",
        version="0.1.0",
        debug=settings.app.debug,
        docs_url="/docs",
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

    return application


app = create_app()

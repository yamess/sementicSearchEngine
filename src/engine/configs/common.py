from typing import Optional

from pydantic import BaseSettings, Field
from dotenv import find_dotenv


class CommonSettings(BaseSettings):
    class Config:
        env_file = find_dotenv()
        env_file_encoding = "utf-8"
        orm_mode = True


class QDrantSettings(CommonSettings):
    host: str = Field(..., env="VECTOR_DB_HOST")
    port: int = Field(..., env="VECTOR_DB_PORT")
    collection: str = Field(..., env="VECTOR_COLLECTION_NAME")
    embedding_size: int = Field(..., env="VECTOR_EMBEDDING_SIZE")


class BlobSettings(CommonSettings):
    conn_str: str = Field(..., env="AZURE_STORAGE_CONNECTION_STRING")
    container_name: str = Field(..., env="AZURE_CONTAINER")
    account_name: str = Field(..., env="AZURE_ACCOUNT_NAME")
    account_key: str = Field(..., env="AZURE_STORAGE_ACCESS_KEY")
    blob_name: str = Field(..., env="AZURE_BLOB_NAME")


class AppSettings(CommonSettings):
    host: str = Field(..., env="APP_HOST")
    port: int = Field(..., env="APP_PORT")
    debug: bool = Field(..., env="DEBUG")
    reload: bool = Field(..., env="RELOAD")


class ModelSettings(CommonSettings):
    pretrained_model_name: str = Field(..., env="PRETRAINED_MODEL_NAME")


class GlobalSettings(CommonSettings):
    app: Optional[AppSettings] = None
    model: Optional[ModelSettings] = None
    qdrant: Optional[QDrantSettings] = None
    blob: Optional[BlobSettings] = None

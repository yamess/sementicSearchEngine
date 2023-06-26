from pydantic import BaseModel


class Payload(BaseModel):
    id: str
    vector: list[float]
    payload: dict

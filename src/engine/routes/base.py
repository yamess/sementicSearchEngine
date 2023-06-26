from fastapi import APIRouter

route = APIRouter()


@route.get("/health")
async def health():
    return {"message": "Welcome to the search engine service"}

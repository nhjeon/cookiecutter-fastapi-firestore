from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import APIKeyHeader

from api import item

api_router = APIRouter()

API_KEY_SCHEME = APIKeyHeader(name='X-API-KEY')


async def verify_api_key(api_key: str = Depends(API_KEY_SCHEME)):
    if api_key != "fake_api_key":
        raise HTTPException(status_code=400, detail="X-API-KEY header invalid")
    return api_key


api_router.include_router(
    item.router,
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(verify_api_key)],
)

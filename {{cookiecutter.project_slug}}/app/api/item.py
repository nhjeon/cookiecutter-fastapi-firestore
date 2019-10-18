from fastapi import APIRouter

from model.item import ItemCreate, ItemUpdate
from service import item_service

router = APIRouter()  # pylint: disable=invalid-name


@router.get("/")
def read_items():
    return item_service.read_items()


@router.get("/{item_id}")
def read_item(item_id: str):
    return item_service.read_item(item_id)


@router.post("/")
def create_item(item: ItemCreate):
    return item_service.create_item(item)


@router.put("/{item_id}")
def update_item(item_id: str, item: ItemUpdate):
    return item_service.update_item(item_id, item)


@router.delete("/{item_id}")
def delete_item(item_id: str):
    return item_service.delete_item(item_id)

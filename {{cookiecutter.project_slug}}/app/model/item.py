from datetime import datetime

from model.doc_model_base import DocModelBase


class ItemBaseInDB(DocModelBase):
    __table_name__ = "items"


class Item(ItemBaseInDB):
    item_id: str
    name: str
    create_time: datetime = datetime.utcnow()
    update_time: datetime = None


class ItemCreate(ItemBaseInDB):
    item_id: str
    name: str


class ItemUpdate(ItemBaseInDB):
    name: str
    update_time: datetime = datetime.utcnow()

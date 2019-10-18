from datetime import datetime

from google.api_core.datetime_helpers import DatetimeWithNanoseconds

from model.doc_model_base import DocModelBase


class ItemBaseInDB(DocModelBase):
    __table_name__ = "items"


class Item(ItemBaseInDB):
    item_id: str = None
    name: str = None
    create_time: DatetimeWithNanoseconds = datetime.utcnow()
    update_time: DatetimeWithNanoseconds = None

    class Config:
        json_encoders = {DatetimeWithNanoseconds: lambda dt: dt.rfc3339()}


class ItemCreate(ItemBaseInDB):
    item_id: str
    name: str


class ItemUpdate(ItemBaseInDB):
    name: str
    update_time: DatetimeWithNanoseconds = datetime.utcnow()

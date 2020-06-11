from database.db import db
from model.item import Item, ItemCreate, ItemUpdate


def read_items():
    return db.query(model=Item).get_list()


def create_item(item_create: ItemCreate):
    return db.save(obj=item_create, ret_model=Item)


def update_item(item_id: str, item_update: ItemUpdate):
    return db.update(doc_id=item_id, obj=item_update, ret_model=Item)


def delete_item(item_id: str):
    item = read_item(item_id)
    db.delete(obj=item)
    return item


def read_item(item_id: str):
    return db.query(model=Item).get(doc_id=item_id)

from database import db
from model.item import Item, ItemCreate, ItemUpdate


def read_items():
    return db.query(Item).get_list()


def create_item(item_create: ItemCreate):
    return db.save(item_create, Item)


def update_item(item_id: str, item_update: ItemUpdate):
    return db.update(item_id, item_update, Item)


def delete_item(item_id: str):
    item = read_item(item_id)
    db.delete(item)
    return item


def read_item(item_id: str):
    return db.query(Item).get(doc_id=item_id)

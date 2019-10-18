from database import db
from model.item import Item, ItemCreate, ItemUpdate


def read_items():
    return list(map(lambda x: Item(**x), db.query(Item).get_list()))


def create_item(item: ItemCreate):
    return Item(**db.save(item))


def update_item(item_id: str, item: ItemUpdate):
    return Item(**db.update(item_id, item))


def delete_item(item_id: str):
    item = read_item(item_id)
    db.delete(item)
    return item


def read_item(item_id: str):
    return Item(**db.query(Item).get(doc_id=item_id))

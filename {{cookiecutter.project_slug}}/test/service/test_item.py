from app.model.item import ItemCreate
from app.service.item_service import create_item


def test_create_time():
    item = ItemCreate(**{"item_id": "Foo", "name": "Fighters"})
    item2 = create_item(item)
    assert item.item_id == item2.item_id

    item = ItemCreate(**{"item_id": "Foo", "name": "Fighters"})
    item2 = create_item(item)
    assert item.item_id == item2.item_id

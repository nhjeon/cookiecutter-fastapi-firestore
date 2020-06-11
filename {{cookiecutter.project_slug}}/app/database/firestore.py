from google.cloud import firestore


class Query:
    def __init__(self, *, model):
        self.model = model
        self.table_name = model.__table_name__

    def get_collection(self):
        from database.db import db
        return db.db.collection(self.model.__table_name__)

    def get(self, *, doc_id):
        from database.db import db

        docs = (
            db.db.collection(self.model.__table_name__).document(doc_id).get()
        )

        if docs.exists:
            return self.model(**docs.to_dict())

        return None

    def get_list(self):
        from database.db import db

        docs = db.db.collection(self.model.__table_name__).stream()
        return list(map(lambda x: self.model(**x.to_dict()), docs))

    def where(self, field_path, op_string, value):
        docs = (
            self.get_collection().where(field_path, op_string, value).stream()
        )
        return list(map(lambda x: self.model(**x.to_dict()), docs))


class FireStoreDB:
    def __init__(self):
        self.db = firestore.Client()

    query = Query

    def update(self, *, doc_id, obj, ret_model=None):
        _ = (
            self.db.collection(obj.__table_name__)
            .document(doc_id)
            .update(obj.dict())
        )
        new_obj = self.db.collection(obj.__table_name__).document(doc_id).get()
        if ret_model:
            return ret_model(**new_obj.to_dict())

        return new_obj.__class__(**new_obj.to_dict())

    def save(self, *, obj, ret_model=None):
        _ = (
            self.db.collection(obj.__table_name__)
            .document(obj.doc_id)
            .set(obj.dict())
        )

        if ret_model:
            return ret_model(**obj.dict())

        return obj.__class__(**obj.dict())

    def delete(self, *, obj):
        self.db.collection(obj.__table_name__).document(obj.doc_id).delete()

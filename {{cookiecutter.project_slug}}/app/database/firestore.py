import firebase_admin
from firebase_admin import credentials, firestore


class Query:
    def __init__(self, model):
        self.model = model
        self.table_name = model.__table_name__

    def get_collection(self):
        from database import db

        return db.db.collection(self.model.__table_name__)

    def get(self, *, doc_id):
        from database import db

        docs = (
            db.db.collection(self.model.__table_name__).document(doc_id).get()
        )
        return docs.to_dict()

    def get_list(self):
        from database import db

        docs = db.db.collection(self.model.__table_name__).stream()
        return list(map(lambda x: x.to_dict(), docs))


class FireStoreDB:
    def __init__(self):
        import os

        service_account_path = os.getenv(
            'GCP_SERVICE_ACCOUNT', 'app/serviceAccount.json'
        )
        cred = credentials.Certificate(service_account_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()  # pylint: disable=invalid-name

    query = Query

    def update(self, doc_id, obj):
        _ = (
            self.db.collection(obj.__table_name__)
            .document(doc_id)
            .update(obj.dict())
        )
        new_obj = self.db.collection(obj.__table_name__).document(doc_id).get()
        return new_obj.to_dict()

    def save(self, obj):
        _ = (
            self.db.collection(obj.__table_name__)
            .document(obj.doc_id)
            .set(obj.dict())
        )
        return obj.dict()

    def delete(self, obj):
        self.db.collection(obj.__table_name__).document(obj.doc_id).delete()

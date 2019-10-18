from pydantic import BaseModel


class DocModelBase(BaseModel):
    @property
    def doc_id(self):
        doc_id = None
        for i in self.fields:
            if 'id' in i:
                doc_id = getattr(self, i)
                break
        if doc_id is None:
            raise ValueError
        return doc_id

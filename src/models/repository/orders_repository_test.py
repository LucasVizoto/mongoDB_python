from .orders_repository import OrdersRepository


class MockCollection:
    def __init__(self):
        self.insert_one_attributes = {}
        self.find_attributes = {}

    def insert_one(self, input_data: any):
        self.insert_one_attributes["dict"] = input_data

    def find(self, *args):
        self.find_attributes["args"] = args
        

class DbCollectionMock:
    def __init__(self, collection):
        self.collection = collection

    def get_collection(self, collection_name: str):
        return self.collection

def test_insert_document():
    collection = MockCollection()
    db_collection = DbCollectionMock(collection)
    repo = OrdersRepository(db_collection)
    
    doc= {"alguma": "coisa"}
    repo.insert_document(doc)

    
    assert collection.insert_one_attributes["dict"] == doc


def test_select_many_with_properties():
    collection = MockCollection()
    db_collection = DbCollectionMock(collection)
    repo = OrdersRepository(db_collection)

    doc_filter = {"status": "pending"}
    repo.select_many_with_properties(doc_filter)

    assert collection.find_attributes["args"][0] == doc_filter
    assert collection.find_attributes["args"][1] == {"_id": 0, "cupom": 0}
    assert collection.find_attributes["args"] == (doc_filter, {"_id": 0, "cupom": 0})
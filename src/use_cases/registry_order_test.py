from pytest import raises

from src.main.http_types.http_request import HttpRequest
from .registry_order import RegistryOrder

class MockOrderRepository:
    def __init__(self):
        self.insert_document_att = {}
        
    def insert_document(self, document: dict) -> None:
        self.insert_document_att["document"] = document

class MockOrdersRepositoryError:
    def insert_document(self, document: dict) -> None:
        raise Exception("Error inserting document")

mock_request_registry = HttpRequest(
    body={
        "data": {
            "name": "Test Order",
            "address": "123 Test St",
            "cupom": False,
            "items": [
                {"item": "Pizza", "quantity": 2},
                {"item": "Refrigerante", "quantity": 1}
            ]
        }
    }
)

def test_registry():
    repo = MockOrderRepository()

    registry_order = RegistryOrder(repo)

    response = registry_order.registry(mock_request_registry)

    assert "name" in repo.insert_document_att["document"]
    assert "address" in repo.insert_document_att["document"]
    assert "created_at" in repo.insert_document_att["document"]

    assert response.status_code == 201
    assert response.body["data"]["type"] == "Order"
    assert response.body["data"]["count"] == 1
  
    # print(response.body)
    # print(response.status_code)

    # print()
    # print(repo.insert_document_att)

def test_registry_order_error():
    repo_error = MockOrdersRepositoryError()
        

    with raises(Exception) as e:

        registry_order_error = RegistryOrder(repo_error)
        response = registry_order_error.registry(mock_request_registry)

        #print(response.body)
        #print(response.status_code)

        assert response.status_code == 400
        assert "error" in response.body
        assert str(e.value) == "Error inserting document"   
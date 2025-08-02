from .registry_order_validator import registry_order_validator
from pytest import raises

def test_registry_order_validator():
    body = {
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
    registry_order_validator(body)
    
def test_registry_order_validator_invalid():
    body_error ={
        "data": {
            "name": "Test Order",
            "address": "123 Test St",
            "cupom": "false",  # Invalid type 
            "items": [
                {"item": "Pizza", "quantity": 2},
                {"item": "Refrigerante", "quantity": 1}
            ]
        }
    }
    with raises(Exception) as exc_info:
        registry_order_validator(body_error)
        assert str(exc_info.value) == "{'data': {'cupom': ['must be of boolean type']}}"
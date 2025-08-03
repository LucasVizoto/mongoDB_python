from src.models.repository.interfaces.orders_repository_interface import OrdersRepositoryInterface

from src.main.http_types.http_response import HttpResponse
from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.error_handler import error_handler

class RegistryFinder: 
    def __init__(self, orders_repository: OrdersRepositoryInterface):
        self.__orders_repository = orders_repository

    def find(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.path_params["order_id"]
            order = self.__search_order(order_id)
            formatted_response = self.__format_response(order)
            return formatted_response
        
        except Exception as e:
            return error_handler(e)
    
    def __search_order(self, order_id: str) -> dict:
        order = self.__orders_repository.select_by_object_id(order_id)
        if not order:
            raise HttpNotFoundError("Order not Found")
        return order
    
    def __format_response(self, order: dict) -> HttpResponse:
        order["_id"] = str(order["_id"])  # Convert ObjectId to string for JSON serialization
        return HttpResponse(
            body={
                "data": {
                    "type": "Order",
                    "count": 1,
                    "attributes": order
                }
            },
            status_code=200
        )
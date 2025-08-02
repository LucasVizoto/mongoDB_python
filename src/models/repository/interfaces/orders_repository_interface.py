from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def insert_document(self, document: dict)->None:
        ...

    @abstractmethod
    def insert_list_of_documents(self, list_of_documents: list) -> None:
        ...

    @abstractmethod
    def select_many(self, doc_filter: dict) -> list[dict]:
        ...
    
    @abstractmethod
    def select_one(self, doc_filter: dict)->dict:
        ...
    
    @abstractmethod
    def select_many_with_properties(self, doc_filter: dict)->list:
        ...

    @abstractmethod
    def select_if_property_exists(self)->dict:
        ...
    
    @abstractmethod
    def select_by_object_id(self, object_id: str) -> dict:
        ...
    
    @abstractmethod
    def edit_registry(self, order_id: str, update_fields: dict) -> None:
        ...

    @abstractmethod
    def edit_many_registries(self) -> None:
        ...

    @abstractmethod
    def edit_registry_with_increment(self) -> None:
        ...

    @abstractmethod    
    def delete_registry(self) -> None:
        ...
    
    @abstractmethod
    def delete_many_registries(self) -> None:
        ...
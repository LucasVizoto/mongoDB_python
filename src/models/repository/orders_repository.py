from bson.objectid import ObjectId

class OrdersRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = 'orders'
        self.__db_connection = db_connection
       

    def insert_document(self, document: dict)->None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list[dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data
    
    def select_one(self, doc_filter: dict)->dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
        return response
    
    def select_many_with_properties(self, doc_filter: dict)->list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        property_doc = {"_id": 0, "cupom": 0} #opções de retorno
        data = collection.find(
            doc_filter, #filtro de busca
            property_doc #propriedades que serão removidas da response
            )
        return data

    def select_if_property_exists(self)->dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        
        exist_doc = {
            "address": {"$exists": True}
        }

        property_doc = {"_id": 0, "itens": 0}

        data = collection.find(exist_doc, property_doc)
        return data
    
    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({"_id": ObjectId(object_id)})
        return data
    
    def edit_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)

        collection.update_one(
            {"_id": ObjectId('68865a4bfeefe41b27e0b189')}, # dicionário onde eu faço a busca, ou seja filtros
            {"$set": {"itens.refrigerante.quantidade": 18}} # dicionário com os novos dados 
        )

    def edit_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)

        collection.update_many(
            {"itens.refrigerante": {"$exists": True}}, # dicionário onde eu faço a busca, ou seja filtros
            {"$set": {"itens.refrigerante.quantidade": 22}} # dicionário com os novos dados 
        )

    def edit_registry_with_increment(self):
        collection = self.__db_connection.get_collection(self.__collection_name)

        collection.update_one(
            {"_id": ObjectId('68865a4bfeefe41b27e0b189')}, # dicionário onde eu faço a busca, ou seja filtros
            {"$inc": {"itens.refrigerante.quantidade": 1}} #quantidade que vou somar no objeto já existene
        )
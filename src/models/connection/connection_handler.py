from pymongo import MongoClient

class DBConnectionHandler:
    def __init__(self)-> None:
        # self.__connection_string = 'mongodb://{}:{}@{}:{}/?authSource=admin'.format(
        #     "admin", # username
        #     "password", # password
        #     "localhost", # host
        #     "27017"    # port
        # ) Ao tentar conectar usando o padrão passado no vídeo, não obtive sucesso
        # mas a forma correta de fazer a conexão seria através do método acima
        # e não deste outro
        self.__connection_string = 'mongodb://localhost:27017/'
        self.__dabase_name = 'rocket_db'
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self) -> None:
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__dabase_name]

    def get_db_connection(self):
        return self.__db_connection
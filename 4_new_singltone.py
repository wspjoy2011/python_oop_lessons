class Point:
    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ для ' + str(cls))
        return super().__new__(cls)  # возврат объекта из базового класса

    def __init__(self, x=0, y=0):
        print('Вызов __init__ для ' + str(self))
        self.x = x
        self.y = y


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, db_name, user, password, host, port):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.db_name}')

    def close(self):
        print(f'Закрытие соединения с БД: {self.db_name}')

    def read(self):
        print(f'Данные из БД: {self.db_name}')

    def write(self, data):
        print(f'Запись в БД: {self.db_name}.\nДанные: {data}')


point = Point()
database = DataBase('Postgres', 'root', 'password', '127.0.0.1', '8000')
database.connect()
database.write('Какие то данные')

database_new = DataBase('Mysql', 'root', 'password', '127.0.0.1', '8000')
database_new.connect()
database.connect()
print(id(database) == id(database_new))
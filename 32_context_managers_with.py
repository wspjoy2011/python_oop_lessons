# Вариант без менеджера контекста
file = None
try:
    file = open('myfile.txt')
    for line in file.readlines():
        print(line)
except Exception as error:
    print(error)
finally:
    if file is not None:
        file.close()
# Вариант c менеджером контекста
file = None
try:
    with open('myfile.txt') as file:
        for line in file:
            print(line)
except Exception as error:
    print(error)

# менеджер контекста with
# __enter__() - срабатывает в момент создания объекта менеджера контекста
# __exit__() - срабатывает в момент завершения работы менеджера контекста или возникновения исключения


class DefenderVector:
    def __init__(self, vector):
        self.__vector = vector

    def __enter__(self):
        self.__temp = self.__vector[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__vector[:] = self.__temp
        return False


vector1 = [1, 2, 3]
vector2 = [2, 3]

try:
    with DefenderVector(vector1) as dv:
        for i, value in enumerate(dv):
            dv[i] += vector2[i]
except Exception as error:
    print(f'Error: {error}')
finally:
    print(vector1)

# attribute - public публичное свойство
# _attribute - protected служит для обращения внутри класса или в дочерних классах
# __attribute - private служит для обращения только внутри класса
# setter and getter - интерфейсные методы
from accessify import private, protected


class Point:
    MIN_COORDINATE = 0
    MAX_COORDINATE = 100

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_coordinates(x, y):
            self.__x = x
            self.__y = y

    @private  # можно убрать двойное подчеркивание, модификатор доступа
    @classmethod
    def __check_coordinates(cls, x, y):
        return isinstance(x, int | float) and isinstance(y, int | float) and \
               cls.MIN_COORDINATE <= x <= cls.MAX_COORDINATE and cls.MIN_COORDINATE <= y <= cls.MAX_COORDINATE

    def set_coordinates(self, x, y):
        if self.__check_coordinates(x, y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError(f'Аргументы x, y должны быть должны быть числами в диапазоне '
                             f'{self.MIN_COORDINATE} - {self.MAX_COORDINATE}')

    def get_coordinates(self):
        return f'X: {self.__x}, Y: {self.__y}'


point = Point(1, 200)
print(dir(point))
print(point.get_coordinates())
point.set_coordinates(3, 100)
print(point.get_coordinates())
print(point.get_coordinates())

point2 = Point(2, 3)
print(point2.get_coordinates())
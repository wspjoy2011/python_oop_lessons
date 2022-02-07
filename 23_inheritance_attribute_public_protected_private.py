# attribute - свойство public доступное всем
# _attribute - свойство protected доступно только в классах наследниках
# __attribute - свойство private - доступное только из класса которому принадлежит

class Geometry:
    name = 'Geometry'
    __status = 'check'

    def __init__(self, x1, y1, x2, y2):
        self.__verify_coordinate(x1)

        self.__x1 = x1
        self.__y1 = y1
        self._x2 = x2
        self._y2 = y2

    def get_coordinates(self):
        print(self.__x1, self.__y1)

    @classmethod
    def __verify_coordinate(cls, coord):
        return isinstance(coord, int) and 0 <= coord <= 100


class Rectangle(Geometry):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super(Rectangle, self).__init__(x1, x2, y1, y2)
        self.__fill = fill

    def get_coordinates(self):
        super(Rectangle, self).get_coordinates()
        print(f'{self._x2} {self._y2}')


rectangle = Rectangle(1, 1, 2, 2)
print(rectangle.get_coordinates())
print(rectangle.__dict__)
print(rectangle.name)
print(rectangle._Geometry__status)

#  __slots__
# ограничение создаваемых локальных свойств
# уменьшение занимаемой памяти
# ускорение работы с лакальными свойствами
from timeit import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2D:
    __slots__ = ('x', 'y')  # определяет набор свойств которые могут быть у объекта,уменьшает размер в памяти
    MAX_COORDINATE = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate(self):
        self.x += 20 ** 100
        del self.y
        self.y = 0


point = Point(1, 2)
point.z = 100
print(point.__dict__)

point2d = Point2D(3, 4)
point2d.x = 50
# del point2d.y
time1 = timeit(point2d.calculate)
print(time1)
point2d.y = 20
print(point.__sizeof__() + point.__dict__.__sizeof__())
print(point2d.__sizeof__())

# print(point2d.__dict__)  # если есть slots то коллекция dict не формируется
# point2d.z = 30

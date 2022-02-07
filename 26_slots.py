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


point = Point(1, 2)
point.z = 100
print(point.__dict__)

point2d = Point2D(3, 4)
point2d.x = 50
del point2d.y
point2d.y = 20
print(point.__sizeof__() + point.__dict__.__sizeof__())
print(point2d.__sizeof__())
# print(point2d.__dict__)  # если есть slots то коллекция dict не формируется
# point2d.z = 30

from timeit import timeit

class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) ** 0.5  # длина радиус вектора

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value


class Point3D(Point2D):
    __slots__ = ('z',)

    def __init__(self, x, y, z):
        super(Point3D, self).__init__(x, y)
        self.z = z


point2d = Point2D(1, 2)
print(point2d.length)
point3d = Point3D(3, 4, 5)
point3d.z = 10
print(point3d.z)
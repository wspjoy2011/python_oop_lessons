from abc import ABC, abstractmethod


class Geometry(ABC):
    @abstractmethod
    def get_perimeter(self):
        raise NotImplementedError('В жочернем классе должен быть определён метод get_perimeter')


class Rectangle(Geometry):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Geometry):
    def __init__(self, side):
        self.side = side

    def get_perimeter(self):
        return 4 * self.side


class Triangle(Geometry):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        return self.side_a * self.side_b * self.side_c


rectangle1 = Rectangle(1, 2)
rectangle2 = Rectangle(3, 4)
square1 = Square(4)
square2 = Square(5)
triangle1 = Triangle(3, 4, 5)
triangle2 = Triangle(6, 7, 8)

geometry_figures = [rectangle1, rectangle2, square1, square2, triangle1, triangle2]


for figure in geometry_figures:
    print(figure.get_perimeter())

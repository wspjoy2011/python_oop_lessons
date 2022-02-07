class Geometry:
    pass


class Line(Geometry):
    pass


class Vector(list):
    # def __init__(self):
    #     list.__init__(self)

    def __str__(self):
        return ' '.join(map(str, self))


vector = Vector([1, 2, 3])
print(type(vector))
print(vector)

line = Line()

print(Geometry.__name__)
print(line.__class__)
print(issubclass(Line, Geometry))
print(issubclass(Line, object))
print(isinstance(line, Geometry))
print(issubclass(int, object))
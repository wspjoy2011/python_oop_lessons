class Vector:
    MIN_COORDINATE = 0
    MAX_COORDINATE = 100

    @classmethod
    def validate_coordinates(cls, arg):
        return cls.MIN_COORDINATE <= arg <= cls.MAX_COORDINATE

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate_coordinates(x) and self.validate_coordinates(y):
            self.x = x
            self.y = y
        print(Vector.quadratic_form(self.x, self.y))

    def get_coordinates(self):
        return self.x, self.y

    @staticmethod
    def quadratic_form(x, y):
        return x*x + y*y


vector = Vector(5, 6)
print(vector.get_coordinates())
print(Vector.validate_coordinates(5))
print(Vector.get_coordinates(vector))

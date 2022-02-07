class Point:
    color = 'red'
    circle = 2

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


point = Point()
point.set_coordinates(10, 10)
print(point.__dict__)
print(getattr(point, 'z', False))
print(point.get_coordinates())

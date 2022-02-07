class Point:
    x = 5
    y = 6

    def set_coordinates(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Point):
    def draw(self):
        print('Drawing line...')


class Rectangle(Point):
    def draw(self):
        print('Drawing rectangle...')


point = Point()
line = Line()
line.set_coordinates(1, 1, 2, 2)
print(point.x)
print(line.x)
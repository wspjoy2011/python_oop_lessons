class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):  # алгоритм работы __hash__ зависит от __eq__
        return hash((self.x, self.y))


point1 = Point(1, 2)
point2 = Point(1, 1)
print(hash(point1), hash(point2), sep='\n')
print(point1 == point2)

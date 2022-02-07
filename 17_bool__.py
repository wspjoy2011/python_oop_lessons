# __bool__ - зависит от метода __len__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__')
        return self.x ** 2 + self.y ** 2

    def __bool__(self):
        print('__bool__')
        return self.x == self.y


point = Point(1, 2)
print(bool(point))

if point:
    print('Object point True')
else:
    print('Object point False')

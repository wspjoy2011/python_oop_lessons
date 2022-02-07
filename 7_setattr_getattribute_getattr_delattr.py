# __setattr__(self, key, value) - автоматически вызывается при изменении свойства key класса
# __getattribute__(self, item) - автоматически вызывается при получении свойства класса с именем item
# __getattr__(self, item) - автоматически вызывается при обращении к несуществующему свойству item класса
# __delattr__(self, item) - автоматически вызывается при удалении свойства item(не важно существует оно или нет)


class Point:
    MIN_COORDINATE = 0
    MAX_COORDINATE = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORDINATE = left

    def __getattribute__(self, item):
        # print('__getattribute__')
        if item == 'x':  # генерируем ошибку если идёт напрямую обращение к свойству x
            raise ValueError('Доступ запрещён')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print('__setattr__')
        if key == 'z':  # генерируем ошибку если имя свойства z
            raise AttributeError('Недопустимое свойство объекта')
        else:
            object.__setattr__(self, key, value)
            #self.__dict__[key] = value  # прямое присваивание в __dict__

    def __getattr__(self, item):
        print('__getattr__: ' + item)
        return False

    def __delattr__(self, item):
        print('__delattr__: ' + item)
        object.__delattr__(self, item)



point1 = Point(1, 2)
point2 = Point(3, 4)

Point.set_bound(-100)

print(point1.__dict__)
print(Point.__dict__)

y1 = point1.y
del point1.y
# x1 = point1.x
# point1.z = 100
print(point1.j)
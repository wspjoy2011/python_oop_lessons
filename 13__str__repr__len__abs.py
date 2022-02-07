# __str__ - для отображения информации об объекте для пользователя(функции str, print)
# __repr__ - для отображения информации об объекте для разработчиков(консоль пайтон)

class Person:
    def __init__(self, full_name):
        self.full_name = full_name
        print(len(full_name))

    def __repr__(self):
        return f'{self.__class__}: {self.full_name}'

    def __str__(self):
        return f'Full name: {self.full_name}'

    def __len__(self):
        return len(self.full_name)


class Point:
    def __init__(self, *args):
        self.__coordinates = args
        print(self.__coordinates)

    def __len__(self):
        return len(self.__coordinates)

    def __abs__(self):
        return tuple(map(abs, self.__coordinates))


jack = Person('Jack Black')
print(jack)
print(len(jack))

point = Point(-1, 2, 3)
print(len(point))
print(abs(point))
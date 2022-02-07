class Geometry:
    name = 'Geometry'

    def __init__(self, x1, x2, y1, y2):
        print(f'Geometry class initializer for: {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x1 = x2
        self.y2 = y2

    def get_name(self):
        print(self.name)


class Line(Geometry):
    def __init__(self, x1, x2, y1, y2):
        Geometry.__init__(self, x1, y1, x2, y2)
        print('Line class initializer')

    def draw(self): # если метода нет в базовом классе и мы его добавили в дочерний то это расширение функциональности базового класса
        print('Drawing line...')

    def get_name(self): # если метод еть в базовом классе то это называется переопределением метода
        print(f'Name: {self.name}')


class Rectangle(Geometry):
    def __init__(self, x1, x2, y1, y2, fill=None):
        super(Rectangle, self).__init__(x1, y1, x2, y2) # делегирование каких то действий в базовый класс
        self.fill = fill
        print('Rectangle class initializer')

    def draw(self): # если метода нет в базовом классе и мы его добавили в дочерний то это расширение функциональности базового класса
        print('Drawing rectangle...')

    def get_name(self): # если метод еть в базовом классе то это называется переопределением метода
        print(f'Name: {self.name}')


line = Line(1, 1, 2, 2)
rectangle = Rectangle(2, 3 , 10, 15)
print(rectangle.__dict__)
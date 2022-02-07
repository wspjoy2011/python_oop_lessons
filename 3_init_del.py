# __new__ - создаёт новый экземпляр класса, запускается перед __init__
# __init__ - инициализатор, если не указывать то создаётся из мета класса
# __del__ - финализатор

class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        print('Удаление экземпляра класса ' + str(self))

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


point = Point()
print(point.__dict__)
point.set_coordinates(10, 5)
print(point.get_coordinates())

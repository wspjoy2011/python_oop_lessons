class ReadIntX:  # non-data дескриптор
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:  # data дескриптор
    @classmethod
    def verify_coordinate(cls, coordinate):
        if not isinstance(coordinate, int):
            raise TypeError('Координаты должны быть целым числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coordinate(value)
        print(f'__set__: {self.name} = {value}')
        setattr(instance, self.name, value)


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    x_read = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


point = Point3D(2, 3, 4)
print(point.__dict__)
print(point.x_read)
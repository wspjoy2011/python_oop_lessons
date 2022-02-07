# getattr(obj, name, default) - возвращает значение атрибута объекта
# hasattr(obj, name) - проверяет на наличие атрибута в объекте
# setattr(obj, name, value) - задаёт значение атрибута
# delattr(obj, name) - удаляет атрибут с именем name
# object.__doc__ - содержит строку с описанием класса
# object.__dict__ - содержит набор атрибутов класса


class Point:
    """Example of class"""
    color = 'red'
    circle = 2


a = Point()
b = Point()
print(Point.color, a.color, b.color)
print(a.__dict__)
a.color = 'blue'
print(Point.color, a.color, b.color)
print(a.__dict__)
Point.color = 'green'
print(Point.color, a.color, b.color)
Point.shape = 'triangle'
print(a.shape)
setattr(Point, 'property', 10)
print(a.property)
print(getattr(a, 'property', False))
print(Point.__dict__)
print(Point.__doc__)
del Point.property
print(hasattr(Point, 'property'))
delattr(Point, 'circle')
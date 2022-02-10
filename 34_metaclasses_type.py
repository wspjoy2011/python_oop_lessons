# metaclass(type()) -> class -> object
class Point:
    MIN_COORDINATE = 0
    MAX_COORDINATE = 100

class B1:
    pass

class B2:
    pass

def method1(self):
    print(self.__dict__)


A = type('Point', (), {'MIN_COORDINATE': 0, 'MAX_COORDINATE': 100})
print(A)
point = A()
A = type('Point', (B1, B2), {'MIN_COORDINATE': 0, 'MAX_COORDINATE': 100, 'method': method1,
                             'get_max_coord': lambda self: print(self.MAX_COORDINATE)})
print(A.__mro__)
point = A()
point.method()
point.get_max_coord()

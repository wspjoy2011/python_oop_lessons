# type('class', (classes), {attribute|method: value})
# class Point:
#     MIN_COORDINATE = 0
#     MAX_COORDINATE = 100
#
#
# A = type('Point', (), {'MIN_COORDINATE': 0, 'MAX_COORDINATE': 100})


# metaclass as function
# def create_class_point(class_name, base_classes, attributes):
#     attributes.update({'MIN_COORDINATE': 0, 'MAX_COORDINATE': 100})
#     return type(class_name, base_classes, attributes)

# метакласс должен наследоваться от type
class Meta(type):
    def __new__(cls, class_name, base_classes, attributes):
        attributes.update({'MIN_COORDINATE': 0, 'MAX_COORDINATE': 100})
        return type.__new__(cls, class_name, base_classes, attributes)

    def __init__(cls, class_name, base_classes, attributes):
        super().__init__(class_name, base_classes, attributes)
        cls.MIN_COORDINATE = 0
        cls.MAX_COORDINATE = 100


class Point(metaclass=Meta):
    def get_coordinates(self):
        return 0, 0


point = Point()
print(point.MAX_COORDINATE)
print(point.get_coordinates())

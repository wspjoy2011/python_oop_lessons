# Django ORM example
# класс Model выступает метаклассом для Person
# class Person(models.Model):
#     title = models.CharField(max_lenght=255)
#     content = models.TextField(blank=True)
#     photo = models.ImageField(upload_to='photos/Y%/%m/%d/')
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
#
#
# person = Person(title='John Doe')

# Использование метакласса
class Meta(type):
    def create_local_attributes(self, *args, **kwargs):
        for key, value in self.class_attributes.items():
            self.__dict__[key] = value

    def __init__(cls, class_name, base_classes, attributes):
        cls.class_attributes = attributes
        cls.__init__ = Meta.create_local_attributes


class Person(metaclass=Meta):
    title = 'заголовок'
    content = 'содержание'
    photo = 'путь к фото'


person = Person()
print(person.__dict__)


# Тот же результат без метакласса
class Person(metaclass=Meta):
    title = 'заголовок'
    content = 'содержание'
    photo = 'путь к фото'
    class_attributes = {'title': title, 'content': content, 'photo': photo}

    def __init__(self, *args, **kwargs):
        for key, value in self.class_attributes.items():
            self.__dict__[key] = value


person = Person()
print(person.__dict__)
class Person:
    title = 'объект класса для поля title'
    photo = 'объект класса для поля photo'
    ordering = 'объект класса для поля ordering'

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self.meta = self.Meta(f'{username}@{password}')

    class Meta:  # создаём дополнительное пространство имён
        ordering = ['id']

        def __init__(self, access):
            self._access = access
            self._person_title = Person.title  # технически можно из вложеного класса обратиться к
            # атрибутам внешнего класса но логику следует продумывать так что бы из вложеного не обращаться к внешнему


print(Person.ordering)
print(Person.Meta.ordering)

person = Person('test', 'test123')
print(person.ordering)
print(person.Meta.ordering)
print(person.__dict__)
print(person.meta.__dict__)

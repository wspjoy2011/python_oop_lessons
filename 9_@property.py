class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age

    # в аргументах функции указываем getter и setter и можем обращаться к ним как к свойству
    #age = property(fget=get_age, fset=set_age)

    # альтернативный способ с использованием декоратора
    # age = property()
    # age = age.getter(get_age)
    # age = age.setter(set_age)


person = Person('John', 20)
person.age = 25
print(person.__dict__)
print(person.age)


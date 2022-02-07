from string import ascii_letters
from re import match


class Person:
    RUS_LOWER = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    RUS_UPPER = RUS_LOWER.upper()

    def __init__(self, full_name, age, id_card, weight):
        self.verify_full_name(full_name)
        self.verify_age(age)
        self.verify_weight(weight)
        self.verify_id_card(id_card)

        self.__full_name = full_name
        self.__age = age
        self.__id_card = id_card
        self.__weight = weight

    @classmethod
    def verify_full_name(cls, full_name):
        if not isinstance(full_name, str):
            raise TypeError('ФИО должно быть строкой')

        full_name = full_name.split()
        if len(full_name) != 3:
            raise TypeError('Неверный формат ФИО.')

        letters = ascii_letters + cls.RUS_LOWER + cls.RUS_UPPER

        for name in full_name:
            if not name:
                raise TypeError('В ФИО должен быть хотя бы один символ')

            if len(name.strip(letters)) != 0:
                raise TypeError('В ФИО могут быть только буквы')

    @classmethod
    def verify_age(cls, age):
        if not isinstance(age, int):
            raise TypeError('Возраст должен быть указан целым числом')

        if age < 14 or age > 100:
            raise ValueError('Возраст должел быть в промежутке от 14 до 100 лет')

    @classmethod
    def verify_weight(cls, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError('Вес должен быть целым или вещественным числом')

        if weight < 20 or weight > 200:
            raise ValueError('Вес должен быть в диапазоне от 20 до 200')

    @classmethod
    def verify_id_card(cls, id_card):
        if not isinstance(id_card, str):
            raise TypeError('Неверный тип данных для номера паспорта')
        if match(r'\w{2}[-]\d{6}', id_card) is None:
            raise ValueError('Неверный формат данных паспорта XX-XXXXXX')

    @property
    def full_name(self):
        return self.__full_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def id_card(self):
        return self.__id_card

    @id_card.setter
    def id_card(self, id_card):
        self.verify_id_card(id_card)
        self.__id_card = id_card

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__id_card = weight


person = Person('Иванов Иван Иванович', 36, 'ВР-415141', 101.3)
print(person.__dict__)
print(person.full_name)
print(person.age)
print(person.id_card)
print(person.weight)

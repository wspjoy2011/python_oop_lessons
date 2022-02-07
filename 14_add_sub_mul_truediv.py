# __add__() - операция сложение
# __sub__() - операция вычитание
# __mul__() - операция умножение
# __truediv__() - операция деление
# __floordiv__() - операция //
# __mod__() - операция %
from datetime import datetime


class Clock:
    __DAY = 60 * 60 * 24  # число секунд в сутках

    def __init__(self, seconds: int):
        self.verify_data_init(seconds)
        self.seconds = seconds % self.__DAY

    def __add__(self, other: int):
        self.verify_data_math(other)
        second_other = other
        if isinstance(other, Clock):
            second_other = other.seconds
        return Clock(self.seconds + second_other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other: int):
        self.verify_data_math(other)
        return Clock(self.seconds - other)

    @classmethod
    def verify_data_init(cls, data):
        if not isinstance(data, int):
            raise TypeError('Значение секунд должно быть целым числом')

    @classmethod
    def verify_data_math(cls, data):
        if not isinstance(data, (int, Clock)):
            raise ArithmeticError('Правый операнд должен быть int или Clock')

    @classmethod
    def __get_formatted(cls, x_time):
        return str(x_time).rjust(2, '0')

    def get_time(self):
        second = self.seconds % 60
        minute = (self.seconds // 60) % 60
        hour = (self.seconds // 3600) % 24
        return f'{self.__get_formatted(hour)}:{self.__get_formatted(minute)}:{self.__get_formatted(second)}'


clock1 = Clock(1000)
clock2 = Clock(1500)
clock1 += 100
clock1 -= 10
clock1 = 100 + clock1
clock1 += clock2
print(clock1.get_time())

my_time = '2022-Jan-31 00:00:00'
time_delta = datetime.now() - datetime.strptime(str(my_time), '%Y-%b-%d %H:%M:%S')

clock2 = Clock(round(time_delta.total_seconds()))
print(clock2.get_time())

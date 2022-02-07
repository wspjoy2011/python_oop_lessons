# __eq__ - равенство ==
# __ne__ - неравенство !=
# __lt__ - для оператора меньше <
# __le__ - для оператора меньше равно <=
# __gt__ - для оператора больше >
# __ge__ - для оператора больше или равно >=

class Clock:
    __DAY = 60 * 60 * 24

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Seconds must be an integer')
        self.seconds = seconds

    @classmethod
    def __verify_date(cls, other):
        if not isinstance(other, (Clock, int)):
            raise TypeError('The right operand must be an instance of a class Clock or int')
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        return self.seconds == self.__verify_date(other)

    def __lt__(self, other):
        return self.seconds < self.__verify_date(other)

    def __le__(self, other):
        return self.seconds <= self.__verify_date(other)


clock1 = Clock(1000)
clock2 = Clock(1000)
print(clock1 < clock2)
print(clock1 == 1000)
print(clock1 <= 1000)


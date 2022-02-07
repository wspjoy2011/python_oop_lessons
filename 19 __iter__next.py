# __iter__ - получение итератора для перебора объекта
# __next__ - переход к следующему значению

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step
        self.value = self.start - self.step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.frange = FRange(start, stop, step)
        self.rows = rows

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.rows:
            self.value += 1
            return iter(self.frange)
        else:
            raise StopIteration


frange = FRange2D(0, 2, 0.5)
# frange_iter = iter(frange)
for row in frange:
    for number in row:
        print(number, end=' ')
    print()

# numbers = list(range(5))
# numbers_iter = iter(numbers)
# print(next(numbers_iter))
# print(next(numbers_iter))

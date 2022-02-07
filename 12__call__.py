from math import sin, pi


class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        print('__call__')
        if not isinstance(args[0], str):
            raise TypeError('Аргумент должен быть строкой')
        self.__counter += 1
        return args[0].strip(self.__chars)


class Derivative:
    def __init__(self, func):
        self.__counter = 0
        self.__func = func

    def __call__(self, x, delta_x=0.0001, *args, **kwargs):
        return (self.__func(x + delta_x) - self.__func(x)) / delta_x


@Derivative
def delta_func_sin(x):
    return sin(x)


print(delta_func_sin(pi / 4))
# delta_func_sin = Derivative(delta_func_sin)
print(delta_func_sin(pi / 4))


strip1 = StripChars('?:;.,! ')
strip2 = StripChars(' ')
result1 = strip1('? Hello, world!')
result2 = strip2('   Hello, world!    ')
print(result1, result2, sep='\n')







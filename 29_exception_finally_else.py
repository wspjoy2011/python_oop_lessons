try:
    x, y = map(int, input('Enter two numbers: ').split())
    result = x / y
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)

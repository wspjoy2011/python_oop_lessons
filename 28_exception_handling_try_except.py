# исключение в момент исполнения - например 10/0 ZeroDivisionError
# исключение в момент компиляции(до исполнения кода) - например неправильный отступ

filename = 'myfile.txt'
try:
    file = open(filename)
except FileNotFoundError:
    file = None
finally:
    if file is not None:
        print(file.readlines())
    else:
        print(f'File {filename} not found')

try:
    x, y = map(int, input('Enter two numbers: ').split())
    result = x / y
except (ValueError, ZeroDivisionError):
    print('Invalid data format or second number was zero')
except BaseException:
    print('Unknown error')
finally:
    print('Finally block')

# with open(filename) as txt:
#     print(txt.readlines())

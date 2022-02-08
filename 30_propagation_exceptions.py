# распространение исключений ошибка будет и в строке вызова функции и в самой функции
# в данном примере у нас есть стек распространения исключений main -> call_calculate -> calculate
# обрабатовать исключения можно на любом уровне стека
def calculate():
    try:
        return 1 / 0
    except:
        print('func calculate error')

def call_calculate():
    try:
        return calculate()
    except:
        print('func call_calculate error')

print('Line1')
print('Line2')
try:
    call_calculate()
except:
    print('func error')
print('Line3')
print('Line4')
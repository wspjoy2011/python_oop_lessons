class ExceptionPrint(Exception):
    """General printer exception class"""


class ExceptionPrintSendData(ExceptionPrint):
    """Exception class when sending data to printer"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'Error: {self.message}'


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'Print: {data}')

    def send_data(self, data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData('Printer is not available')

    def send_to_print(self, data):
        return False


print_doc = PrintData()
try:
    print_doc.print('Important document')
except ExceptionPrintSendData:
    print('Printer is not available')
except ExceptionPrint:
    print('General print error')

print('Line 1')
print('Line 2')
zero = ZeroDivisionError('zero division error')
try:
    1 / 0
except ZeroDivisionError:
    raise zero
print('Line 3')
print('Line 4')

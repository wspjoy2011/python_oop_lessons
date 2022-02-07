from datetime import datetime


class Goods:
    def __init__(self, name, weight, price):
        super().__init__('good')
        print('init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


class MixinLog:
    ID = 0

    def __init__(self, argument):
        super().__init__('first', 'second')
        print('init MixinLog')
        MixinLog.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f'{self.id} был продан в {dt_string}')

    def print_info(self):
        print(f'{self.name}: print_info был вызван из класса MixinLog')


class MixinLog2:
    def __init__(self, argument1, argument2):
        super().__init__()
        print('init MixinLog2')


class Notebook(Goods, MixinLog, MixinLog2):
    def print_info(self):
        MixinLog.print_info(self)


acer = Notebook('Acer', 1.4, 15000)
asus = Notebook('Asus', 1.2, 20000)

acer.print_info()
asus.print_info()

acer.save_sell_log()
asus.save_sell_log()
print(Notebook.__mro__)



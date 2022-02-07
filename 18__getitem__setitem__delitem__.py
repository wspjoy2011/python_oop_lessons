# __getitem__(self, item) - получение значения по ключу item
# __setitem__(self, key, value) - запись значения value по ключу key
# __delitem__(self, key) - удаление значения по ключу key

class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def verify_item(self, item):
        if item >= len(self.marks):
            raise IndexError('Non-existent index')

    @classmethod
    def verify_item_key(cls, key):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Key must be non negative and int type')

    def __getitem__(self, item):
        print('__getitem__')
        self.verify_item(item)
        return self.marks[item]

    def __setitem__(self, key, value):
        print('__setitem__')
        self.verify_item_key(key)

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value

    def __delitem__(self, key):
        self.verify_item_key(key)
        del self.marks[key]

    def __str__(self):
        return str(self.marks)


student = Student('John', [5, 3, 4, 2, 5])
print(student)
student[100] = 5
print(student)
del student.marks[0]
print(student)
class Iterable:
    MAX_VALUE = 10

    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < Iterable.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


class CustomIterator:
    def __iter__(self):
        return Iterable()




c = CustomIterator()  # створено об'єкт, що ітерується.
for i in c:  # зустрівся ітераційний контекст (цикл for) та об'єкт, що ітерується, в ньому, екземпляр класу c
    print(i)

c = CustomIterator()  # створено об'єкт, що ітерується.
for i in c:  # зустрівся ітераційний контекст (цикл for) та об'єкт, що ітерується, в ньому, екземпляр класу c
    print(i)
    print(i)
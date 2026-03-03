class SimpleCounter:
    def __init__(self):
        self.current = 0   # состояние

    def __iter__(self):
        return self        # говорим for: "я сам итератор"

    def __next__(self):
        if self.current < 3:
            self.current += 1
            return self.current
        else:
            raise StopIteration
        
for number in SimpleCounter():
    print(number)
    print(number)
    print(number)
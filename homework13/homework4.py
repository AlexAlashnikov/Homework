class EvenRange:
    """Класс для вывода четных чисел"""
    def __init__(self, start: int, stop: int, step: int=2) -> int:
        self.start = start
        self.stop = stop+1
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self

    def __next__(self):
        if self.start % 2 == 0 and self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        if self.start % 2 != 0 and self.value + self.step < self.stop:
            self.value += self.step
            return self.value+1
        else:
            raise StopIteration

fr = EvenRange(2, 10)
for i in fr:
    print(i)
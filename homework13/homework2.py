class MySquareIterator:
    """Класс возведения в квадрат коллекции чисел."""
    def __init__(self, collection: list):
        self.coll = collection
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = []
        for i in self.coll:
            result.append(i**2)
            if self.count < len(self.coll):
                self.count += 1
            else:
                raise StopIteration
        return result

ls1 = [1,2,3,4,5,7]
iter = MySquareIterator(ls1)
for i in iter:
    print(i)
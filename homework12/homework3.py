class InvalidIntDivision(Exception):
    pass

class InvalidIntNumberCount(Exception):
    pass

class InvalidFloat(Exception):
    pass

class InvalidTextLength(Exception):
    pass

class DuplicatesInText(Exception):
    pass


class Queue:

    def __init__(self):
        self.queue = []

    def add(self, *args):
        for item in args:
            if isinstance(item, int):
                if item % 8:
                    raise InvalidIntNumberCount(f"-> {item} не делиться на 8")
                else:
                    self.queue.append(item)
            if isinstance(item, float):
                if len(str(item)) > len(f"{item:.2f}"):
                    raise InvalidFloat(f"-> {item} больше 2 символов после запятой")
                else:
                    self.queue.append(item)
            if isinstance(item, str):
                if len(item) > 4:
                    raise InvalidTextLength(f"-> {item} больше 4 символов")
                for i in item:
                    coun = item.count(i)
                if coun > 1:
                    raise DuplicatesInText(f"-> {item} больше {coun} символов")
                else:
                    self.queue.append(item)
        return self.queue


q = Queue()
q.add(16, 32, 12.22, 'tex')

print(q.queue)
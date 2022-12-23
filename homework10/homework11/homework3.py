from dataclasses import dataclass
from typing import Any

@dataclass
class DataObject:
    data: Any

class Deque:
    """Класс очередь"""
    deque = []

    @classmethod
    def append_left(cls, data):
        """Добавляет элемент в начало очереди"""
        cls.deque.insert(0, data)
        return cls.deque

    @classmethod
    def append_right(cls, data):
        """Добавляет элемент в конец очереди"""
        cls.deque.append(data)
        return cls.deque

    def pop_left(self):
        """Удаляет элемент из начало очереди,
            получилось только так, через класс-метод никак."""
        return self.deque.pop(0)

    def pop_right(self):
        """Удаляет элемент из конца очереди"""
        return self.deque.pop(-1)


data = DataObject(12)
data1 = DataObject(1)
data2 = DataObject(3)

deque = Deque()
deque.append_left(data)
deque.append_left(data1)
deque.append_right(data2)
print(deque.deque)
deque.pop_right()
print(deque.deque)
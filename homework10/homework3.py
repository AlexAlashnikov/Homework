class Counter:
    """Класс для подсчета значений."""
    def __init__(self, initial_value = 0, stop_value = 0):
        self.initial_value = initial_value
        self.stop_value = stop_value
        if stop_value == 0:
            while True:
                self.stop_value += 1
                print(self.stop_value)
        else:
            print("Maximal value is reached")

    def increment(self):
        self.initial_value += 1

    def get(self):
        print(self.initial_value)

count = Counter(initial_value=29, stop_value=2)
count.increment()
count.get()
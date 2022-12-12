def fibonacci():
    """Бесконечная генерация чисел Фибоначчи"""
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur


for i in fibonacci():
    print(i)

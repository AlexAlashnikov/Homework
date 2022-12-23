class Auto:
    """Инициализация класса Авто."""
    color = 'black'
    weight = 2800
    def __init__(self, brand, age, mark) -> None:
        self.brand = brand
        self.mark = mark
        self.age = age

    def car_information(self):
        print(f"Brand car: {self.brand.title()}; \nMark: {self.mark.title()};"
            f"\nColor: {self.color.title()};\nWeight: {self.weight}.")

    def drive(self):
        print(f"Car {self.brand.title()} {self.mark.title()} drives!")

    def stop(self):
        print(f"Car {self.brand.title()} {self.mark.title()} stops!")

    def use(self):
        self.ages = self.age + 1
        print(f"Car {self.brand.title()} {self.mark.title()} {self.ages} years!")


class Truck(Auto):
    """Наследование класса Авто."""
    def __init__(self, brand, age, mark, max_load) -> None:
        super().__init__(brand, age, mark)
        self.max_load = max_load
        print(f"Max loads: {self.max_load} kg.")

    def drive(self):
        print('Attention!!!')
        return super().drive()

    def load(self):
        import time
        time.sleep(1)
        print("load")
        time.sleep(1)


class Sedan(Auto):
    """Наследование класса Авто."""
    def __init__(self, brand, age, mark) -> None:
        super().__init__(brand, age, mark)

    def max_speeds(self, max_speed):
        self.max_speed = max_speed

    def drive(self):
        super().drive()
        print(f"Max speed of sedan {self.brand.title()}" 
            f" {self.mark.title()} is {self.max_speed} km!\n")



audi_car = Sedan('audi', 18, 'a4')
audi_car.car_information()
audi_car.use()
audi_car.max_speeds(120)
audi_car.drive()

subaru_car = Sedan('subaru', 15, 'impreza')
subaru_car.car_information()
subaru_car.use()
subaru_car.max_speeds(150)
subaru_car.drive()

ford_car = Truck('ford', 16, 'mondeo', 1500)
ford_car.car_information()
ford_car.use()
ford_car.drive()
ford_car.load()



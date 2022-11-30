class Auto:
    """Инициализация класса авто."""
    color = 'black'
    weight = 2800
    def __init__(self, brand, age, mark) -> None:
        self.brand = brand
        self.mark = mark
        self.age = age

    def car_information(self):
        print(f"Brand car: {self.brand.title()}; \nMark: {self.mark.title()};"
            f" \nColor: {self.color.title()}; \nWeight: {self.weight}.")

    def drive(self):
        print(f"Car {self.brand.title()} {self.mark.title()} drives!")

    def stop(self):
        print(f"Car {self.brand.title()} {self.mark.title()} stops!")

    def use(self):
        self.ages = self.age + 1
        print(f"Car {self.brand.title()} {self.mark.title()} {self.ages} years!")

my_car = Auto('audi', 12, 'a8')
my_car.car_information()
my_car.drive()
my_car.stop()
my_car.use()
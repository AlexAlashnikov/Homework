from dataclasses import dataclass

@dataclass
class Dish:
    """Класс хранения данных о блюдах"""
    amount: int
    dish_name: str
    dish_weight: int
    dish_price: float

class Order:
    """Класс Заказ"""
    def __init__(self):
        self.order = []

    def add_dish(self, dish):
        """Метод добавление блюд в заказ"""
        self.order.append(dish)
        return self.order

    @property
    def amounts_dish(self):
        """Общее колличество блюд"""
        amount = sum([i.amount for i in self.order])
        return f"Колличество блюд заказа: {amount}."

    @property
    def order_price(self):
        """Общая сумма блюд"""
        self.price = sum([i.dish_price for i in self.order])
        return f"Сумма заказа: {self.price} руб!"

    @property
    def weight_of_dishes(self):
        """Общий вес блюд"""
        weight = sum([i.dish_weight for i in self.order])
        return f"Общий вес заказа: {weight} грамм."

    def pay(self, money: float):
        """Метод расчета за заказ"""
        if money < self.price:
            print(f"Сумма заказа {self.price}, вы внесли {money}.")
        elif money > self.price:
            residue = money - self.price
            print(f"Ваша здача {residue:.1f}.")

dish1 = Dish(1, 'burger', 90, 3.5)
dish2 = Dish(1, 'pizza', 120, 7.3)

order1 = Order()
order1.add_dish(dish1)
order1.add_dish(dish2)

print(order1.amounts_dish)
print(order1.weight_of_dishes)
print(order1.order_price)
order1.pay(11.2)
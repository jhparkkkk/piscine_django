class HotBeverage:
    def __init__(self, name="hot beverage", price=0.30):
        self.Name = name
        self.Price = price

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self) -> str:
        return f"name: {self.Name}\nprice: {self.Price: .2f}\ndescription: {self.description()}\n"


class Coffee(HotBeverage):
    def __init__(self):
        super().__init__(name="coffee", price=0.40)

    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        super().__init__(name="tea", price=0.30)


class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__(name="chocolate", price=0.50)

    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__(name="cappuccino", price=0.45)

    def description(self):
        return "Un po’ di Italia nella sua tazza!"


if __name__ == "__main__":
    hot_beverage = HotBeverage()
    print(hot_beverage.__str__())

    coffee = Coffee()
    print(coffee.__str__())

    tea = Tea()
    print(tea.__str__())

    chocolate = Chocolate()
    print(chocolate.__str__())

    cappuccino = Cappuccino()
    print(cappuccino.__str__())

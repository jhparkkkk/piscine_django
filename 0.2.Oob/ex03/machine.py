from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random


class CoffeeMachine:
    """
    Coffee machine thats serves different beverages

    Raises:
        self.BrokenMachineException: if Machine exceeded maximum number of servings.

    """

    _nb_servings = 0
    __nb_max_servings = 10

    def __init__(self):
        """
        Set number of servings to zero.
        """
        self.repair()

    class EmptyCup(HotBeverage):
        """
        Represents an empty cup by might be served randomly by the machine

        Args:
            HotBeverage (class): inherits from this parent class.
        """

        def __init__(self):
            super().__init__(name="empty cup", price=0.90)

        def description(self):
            """
            Specific description for a empty cup.

            Returns:
                str: its description
            """
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        """
        Exception raised when the coffee machine \
        needs to be repaired after a certain number of servings.

        Args:
            Exception (_type_): _description_
        """

        def __init__(self):
            super().__init__("This coffee machine has to be repaired.\n")

    def repair(self):
        """
        Resets the number of servings to zero
        """
        self._nb_servings = 0
        print("The coffee machine has been repaired.\n")

    def serve(self, beverage=HotBeverage):
        """
        Serves a hot beverage or an empty cup.

        Args:
            beverage (class, optional): instance of hot beverage to serve. Defaults to HotBeverage.

        Raises:
            self.BrokenMachineException: if the machine has exceeded its number of servings.

        Returns:
            HotBeverage: instance of either the requested beverage or EmptyCup
        """
        if self._nb_servings >= self.__nb_max_servings:
            raise self.BrokenMachineException

        self._nb_servings += 1
        return random.choice((beverage, self.EmptyCup))()


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    hot_beverages = [Coffee, Chocolate, Tea, Cappuccino]

    try:
        while True:
            print(coffee_machine.serve(random.choice(hot_beverages)))
    except coffee_machine.BrokenMachineException as e:
        print(e)

    print(coffee_machine.repair())
    print(coffee_machine.serve(random.choice(hot_beverages)))
    print(coffee_machine.serve(random.choice(hot_beverages)))

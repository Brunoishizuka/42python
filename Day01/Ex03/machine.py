import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino, EmptyCup

class CoffeeMachine:
    def __init__(self):
        self.drinks_served = 0
        self.broken = False

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.drinks_served = 0
        self.broken = False
        print("The coffee machine has been repaired.")

    def serve(self, drink):
        if self.broken:
            raise CoffeeMachine.BrokenMachineException()

        self.drinks_served += 1
        if self.drinks_served > 10:
            self.broken = True
            raise CoffeeMachine.BrokenMachineException()

        if random.choice([True, False]):
            return drink()
        else:
            return EmptyCup()

# Test the CoffeeMachine
if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    try:
        while True:
            served_drink = coffee_machine.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino]))
            print("Served drink:", served_drink)
    except CoffeeMachine.BrokenMachineException:
        print("The coffee machine is broken!")
        choice = input("Do you want to repair it? (yes/no): ")
        if choice.lower() == "yes":
            coffee_machine.repair()
        else:
            print("Goodbye!")

class HotBeverage:
    def __init__(self):
        self.name = "hot beverage"
        self.price = 0.30
    
    def description(self):
        return "Just some hot water in a cup."
    
    def __str__(self):
        return f"name: {self.name}\nprice: {self.price:.2f}\ndescription: {self.description()}"

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "café"
        self.price = 0.40
    
    def description(self):
        return "Um café, para ficar acordado."

class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "chá"

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "chocolate quente"
        self.price = 0.50
    
    def description(self):
        return "Chocolate, doce chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45
    
    def description(self):
        return "Um pouco da Itália na sua xícara!"

class EmptyCup(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "empty cup"
        self.price = 0.90

    def description(self):
        return "An empty cup?! Gimme my money back!"

    def __str__(self):
        return f"name: {self.name}\nprice: {self.price:.2f}\ndescription: {self.description()}"

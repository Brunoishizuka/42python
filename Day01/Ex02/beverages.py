class BebidaQuente:
    def __init__(self):
        self.nome = "bebida quente"
        self.preco = 0.30
    
    def descricao(self):
        return "Apenas um pouco de água quente em uma xícara."
    
    def __str__(self):
        return f"nome: {self.nome}\npreço: {self.preco:.2f}\ndescrição: {self.descricao()}"

class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()
        self.nome = "café"
        self.preco = 0.40
    
    def descricao(self):
        return "Um café, para ficar acordado."

class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()
        self.nome = "chá"

class ChocolateQuente(BebidaQuente):
    def __init__(self):
        super().__init__()
        self.nome = "chocolate quente"
        self.preco = 0.50
    
    def descricao(self):
        return "Chocolate, doce chocolate..."

class Cappuccino(BebidaQuente):
    def __init__(self):
        super().__init__()
        self.nome = "cappuccino"
        self.preco = 0.45
    
    def descricao(self):
        return "Um pouco da Itália na sua xícara!"

def obter_bebida():
    while True:
        print("Escolha uma bebida: café, chá, chocolate quente, cappuccino")
        escolha = input("Digite sua escolha: ").lower()
        if escolha in ["café", "chá", "chocolate quente", "cappuccino"]:
            return escolha
        else:
            print("Escolha inválida. Por favor, escolha novamente.")

def main():
    escolha = obter_bebida()

    if escolha == "café":
        bebida = Cafe()
    elif escolha == "chá":
        bebida = Cha()
    elif escolha == "chocolate quente":
        bebida = ChocolateQuente()
    elif escolha == "cappuccino":
        bebida = Cappuccino()

    print(bebida)

if __name__ == "__main__":
    main()

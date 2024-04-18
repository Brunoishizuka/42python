import sys

def exibir_capital(estado):
    # Dicionários contendo as abreviações dos estados e suas capitais
    estados = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capitais = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # Converter o nome do estado para maiúscula na primeira letra para corresponder às chaves do dicionário
    estado = estado.title()

    # Verificar se o estado existe no dicionário de estados
    if estado in estados:
        # Obter a abreviação do estado
        abreviacao = estados[estado]

        # Verificar se a abreviação existe no dicionário de capitais
        if abreviacao in capitais:
            # Exibir a capital do estado fornecido
            print(capitais[abreviacao])
            return

    # Se o estado não estiver presente nos dicionários, exibir uma mensagem de estado desconhecido
    print("Estado desconhecido")

# Verificar se foi fornecido pelo menos um argumento (exceto o nome do script)
if len(sys.argv) >= 2:
    # Obter todos os argumentos fornecidos após o nome do script
    estado_fornecido = ' '.join(sys.argv[1:])
    exibir_capital(estado_fornecido)
else:
    print("Nenhum argumento fornecido")

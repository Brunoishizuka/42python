import sys

def exibir_estado(cidade):
    # Dicionários contendo as capitais dos estados e suas abreviações
    capitais = {
        "Salem": "OR",
        "Montgomery": "AL",
        "Trenton": "NJ",
        "Denver": "CO"
    }
    estados = {
        "OR": "Oregon",
        "AL": "Alabama",
        "NJ": "New Jersey",
        "CO": "Colorado"
    }

    # Converter a capital para maiúscula na primeira letra para corresponder às chaves do dicionário
    cidade = cidade.title()

    # Verificar se a capital existe no dicionário de capitais
    if cidade in capitais:
        # Obter a abreviação do estado correspondente à capital
        abreviacao = capitais[cidade]

        # Verificar se a abreviação existe no dicionário de estados
        if abreviacao in estados:
            # Exibir o estado correspondente à capital fornecida
            print(estados[abreviacao])
            return

    # Se a capital não estiver presente nos dicionários, exibir uma mensagem de capital desconhecida
    print("Capital desconhecida")

# Verificar se foi fornecido pelo menos um argumento (exceto o nome do script)
if len(sys.argv) >= 2:
    # Obter todos os argumentos fornecidos após o nome do script
    capital_fornecida = ' '.join(sys.argv[1:])
    exibir_estado(capital_fornecida)
else:
    print("Nenhuma capital fornecida")

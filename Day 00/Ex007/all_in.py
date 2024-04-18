# Dicionário que mapeia estados aos seus respectivos capitais
states_capitals = {
    "Oregon": "Salem",
    "California": "Sacramento",
    "Texas": "Austin",
    "New Jersey": "Trenton",
    "New York": "Albany"
}

# Função para detectar se uma expressão é uma capital, um estado ou nenhuma das duas
def detect_expression(expression):
    # Remova espaços em branco no início e no final, e capitalize a expressão
    expression = expression.strip().replace(" ", "").title()
    
    # Verificar se a expressão é uma capital
    if expression in states_capitals.values():
        for state, capital in states_capitals.items():
            if capital == expression:
                return f"{capital} is the capital of {state}"
    
    # Verificar se a expressão é um estado
    elif expression in states_capitals.keys():
        return f"{states_capitals[expression]} is the capital of {expression}"
    
    # Caso a expressão não seja nem uma capital nem um estado
    else:
        # Verificar se a expressão está no formato "State, Capital"
        parts = expression.split(',')
        if len(parts) == 2:
            state, capital = parts[0], parts[1]
            if state.strip().title() in states_capitals.keys() and capital.strip().title() == states_capitals[state.strip().title()]:
                return f"{capital.strip()} is the capital of {state.strip()}"
        return f"{expression} is neither a capital city nor a state"

# Função principal que processa todas as expressões fornecidas
def all_in(expressions):
    results = []
    # Verificar se há pelo menos uma vírgula na entrada e se não há apenas espaços em branco
    if expressions.count(',') > 0 and expressions.replace(',', '').strip() != "":
        # Dividir as expressões na vírgula
        expressions = expressions.split(',')
        # Iterar sobre cada expressão
        for expression in expressions:
            # Verificar se a expressão não está em branco
            if expression.strip() != "":
                # Chamar a função detect_expression para processar a expressão e adicionar o resultado à lista de resultados
                results.append(detect_expression(expression))
    return results

# Bloco principal que verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    import sys
    # Verificar se há exatamente dois argumentos passados ​​(o nome do script e a expressão)
    if len(sys.argv) == 2:
        # Chamar a função all_in com a expressão fornecida como argumento e obter os resultados
        results = all_in(sys.argv[1])
        # Imprimir os resultados
        for result in results:
            print(result)


##Comando Utilizado para teste:  python3 all_in.py "Trenton, Oregon, California, Texas"
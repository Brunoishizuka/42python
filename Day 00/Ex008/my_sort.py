músicos = {
    'Hendrix': '1942',
    'Allman': '1946',
    'King': '1925',
    'Clapton': '1945',
    'Johnson': '1911',
    'Berry': '1926',
    'Vaughan': '1954',
    'Cooder': '1947',
    'Page': '1944',
    'Richards': '1943',
    'Hammett': '1962',
    'Cobain': '1967',
    'Garcia': '1942',
    'Beck': '1944',
    'Santana': '1947',
    'Ramone': '1948',
    'White': '1975',
    'Frusciante': '1970',
    'Thompson': '1949',
    'Burton': '1939',
}

def exibir_músicos_ordenados(músicos):
    """
    Esta função exibe os nomes dos músicos ordenados por ano de nascimento em ordem crescente
    e, dentro de cada ano, ordenados alfabeticamente.
    """
    # Ordenar o dicionário de músicos pelo ano de nascimento
    músicos_ordenados = sorted(músicos.items(), key=lambda x: (x[1], x[0]))
    
    # Imprimir os nomes dos músicos ordenados por ano de nascimento em ordem crescente,
    # e em ordem alfabética para os nascidos no mesmo ano
    for músico, ano in músicos_ordenados:
        print(músico)

# Chamar a função para exibir os músicos ordenados
exibir_músicos_ordenados(músicos)

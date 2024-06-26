def list_to_dict(d):
    """Converte uma lista em um dicionário."""
    dicionario_musicos = {}
    for musico, ano in d: #A variável musico recebe o primeiro elemento e a variável ano recebe o segundo elemento.
        dicionario_musicos[ano] = musico
    return dicionario_musicos

def display_dict(dicionario):
    """Exibe o dicionário na saída padrão."""
    for ano, musico in sorted(dicionario.items()): #Dicionario.items onde a função itens pega da lista do dicionario as possiveis duplas
        print(f"{ano}: {musico}")

# Lista de duplas
d = [
    ('Hendrix', '1942'),
    ('Allman', '1946'),
    ('King', '1925'),
    ('Clapton', '1945'),
    ('Johnson', '1911'),
    ('Berry', '1926'),
    ('Vaughan', '1954'),
    ('Cooder', '1947'),
    ('Page', '1944'),
    ('Richards', '1943'),
    ('Hammett', '1962'),
    ('Cobain', '1967'),
    ('Garcia', '1942'),
    ('Beck', '1944'),
    ('Santana', '1947'),
    ('Ramone', '1948'),
    ('White', '1975'),
    ('Frusciante', '1970'),
    ('Thompson', '1949'),
    ('Burton', '1939')
]

# Converter lista em dicionário
dicionario_musicos = list_to_dict(d)

# Exibir dicionário
display_dict(dicionario_musicos)
"""
Módulo Collections - High-performance Container Datatypes

Ordered Dict (Dicionário Ordenado):
    1. Garante a ordem de execução/inserção


# Em um dicionario comum, a ordem de inserção dos elementos não é garantida...
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'chave = {chave} e valor = {valor}')

# Fazendo o import
from collections import OrderedDict

# Criando o dicionario
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

# Imprimindo elementos
for chave, valor in dicionario.items():
    print(f'chave = {chave} e valor = {valor}')
"""

from collections import OrderedDict
# Entendendo a diferença entre dict e OrderedDict:
# Dicionários comuns:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True: A ordem dos elementos não importa em dicionários comuns

# Ordered Dict:
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False: A ordem faz diferença no OrderedDict!!


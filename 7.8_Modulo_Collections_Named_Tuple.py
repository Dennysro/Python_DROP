"""
Módulo Collections - High-performance Container Datatypes

Named Tuple (Tupla Nomeada):
    1. São tuplas diferenciadas onde especificamos um nome para a mesma
    e também parâmetros

# Relembrando sobre tuplas:
tupla = (1, 2, 3)
print(tupla[1])

"""

# Fazendo o import
from collections import namedtuple

# Definindo o nome e os parâmetros
# Forma 1: Declaração Named Tuple
cachorro = namedtuple('Cachorro', 'idade raca nome')

# Forma 2: Declaração Named Tuple
cachorro2 = namedtuple('Cachorro', 'idade, raca, nome')

# Forma 3: Declaração Named Tuple
cachorro3 = namedtuple('Cachorro', ['idade', 'raca', 'nome'])

# Usando:
info = cachorro(idade=7, raca='Border-Collie', nome='Dommys')
print(info)

# Acessando um elemento:
# Forma 1:
print(info[0])  # Idade
print(info[1])  # Raça
print(info[2])  # Nome

# Forma 2:
print(info.idade)  # Idade
print(info.raca)  # Raça
print(info.nome)  # Nome



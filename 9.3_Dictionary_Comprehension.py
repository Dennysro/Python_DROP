"""
Dictionary Comprehension

Pense no seguinte:
- Se quisermos criar uma lista, fazemos:
    lista = [1, 2, 3, 4]
- Se quisermos criar uma tupla, fazemos:
    tupla = (1, 2, 3, 4)  # 1, 2, 3, 4
- Se quisermos criar um set, fazemos:
    conjunto = {1, 2, 3, 4}
- Se quisermos criar um dicionário, fazemos:
    dict = {'a' : 1, 'b' : 2, 'c': 3, 'd': 4}

# Sintaxe
{chave:valor for valor in iterável}

# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e':5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

# Exemplos
numeros = [1, 2, 3, 4, 5]  # Não podemos ter chaves repetidas em dicionários!
quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

# Exemplos - Brabo pra combinar listas em um dicionário Dennao!
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
"""


# Exemplos com lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)


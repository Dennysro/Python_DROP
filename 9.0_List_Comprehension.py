"""
List Comprehension:
- Utilizando list comprehension nós podemos gerar novas listas com dados processados
    a partir de outro iterável.

    # Sintaxe da List Comprehension
    [dado for dado in iterável]

# Exemplos:
# 1
numeros = [1, 2, 3, 4, 5]
res = [numero*10 for numero in numeros]
print(res)


# Para entender o que o Python faz, vamos dividir a expressão em 2 partes:
# 1- A primeira: for numero in numeros
# 2- A segunda: numero*10


# 2
def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)
"""

# List comprehensions versus Loop
# Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero*2
    numeros_dobrados.append(numero_dobrado)

print(numeros)
print(numeros_dobrados)


# List Comprehension
print([numero*2 for numero in numeros])
# ou
print([numero*2 for numero in [1, 2, 3, 4, 5]])


# Outros Exemplos:
# 1
nome = 'Drop The Beat'
print([letra.upper() for letra in nome])


# 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])


# 3
print([numero*3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])




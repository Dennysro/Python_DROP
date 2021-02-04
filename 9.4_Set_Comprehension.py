"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}

"""

# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo
numero = {x ** 2 for x in range(10)}
print(numero)

# DESAFIO: Faça uma alteração na estrutura acima para gerar um dict
numero = {x: x ** 2 for x in range(10)}
print(numero)

# Pra finalizar
letras = {letra for letra in 'Drop the Beat'}
print(letras)
# Conjuntos não possuem ordenação e não aceitam valores repetidos


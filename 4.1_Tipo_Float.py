"""
Tipo Float
Tipo real, decimal (Casas decimais)
O separador de casas decimais na programação é o ponto e não a virgula (Inglês)
"""

# Errado do ponto de vista Float (Gera uma Tuple)
valor = 1, 44
print(valor)
print(type(valor))

# Certo (Gera um Float)
valor = 1.44
print(valor)
print(type(valor))

# É possível (Dupla declaração)
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Para converter um floar em int
res = int(valor)
print(res)
print(type(res))

# Para trabalhar com números complexos
variavel = 5j
print(variavel**2)




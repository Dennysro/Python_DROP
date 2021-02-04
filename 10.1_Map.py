"""
Map: Fazemos mapeamento de valores para função


import math


def area(r):
    Calcula a area de um círculo com o raio 'r'.
    return math.pi * (r**2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum:
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Utilizando Map:
# Map é uma função que recebe dois parâmetros: 1. Função 2. Iterável
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Utilizando lambda no Map:
print(raios)
print(list(map(lambda f: math.pi * (r**2), raios)))
# OBS: Após a primeira utilização da função map, o resultado zera

"""

# Resumo:
# Temos dados iteráveis
# dados: a1, a2, a3, a4...
# Temos uma função f(x)
# Utilizamos a função map(f(x), dados) onde o map irá 'mapear' cada elemento dos dados e aplicar a função
# O Map Object: f(a1), if f(a2, f(a3), f(n)...

# Mais um exemplo:
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26),
           ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]
print(cidades)


# f = 9/5 * C + 32 (Convertendo de Celsius para F)
# Lambda
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))

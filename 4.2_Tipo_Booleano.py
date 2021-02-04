"""
Tipo Booleano
Álgebra Booleana, criada por George Boole
2 Constantes -> Verdadeiro ou Falso
True -> Verdadeiro
False -> Falso

Errado: true, false
Certo: True, False
"""

ativo = True
print(ativo)

"""
Operações Básicas:
"""

# Negação (not):
"""
Fazendo a negação, se o booleano for verdadeiro o resultado será falso
e se for falso o resultado será verdadeiro. Ou seja, sempre o contrário
"""
print(not ativo)


# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. 
Ou um ou outro deve ser verdadeiro.
True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
ativo = True
logado = False
print(ativo or logado)


# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos os valores devem ser verdadeiros.
True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""


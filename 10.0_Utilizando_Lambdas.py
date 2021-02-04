"""
Utilizando Lambdas

Conhecidas por expressões Lambdas ou simplesmente lambdas, são funções sem nome.
Ou seja, anônimas.

#Função em Python:
def soma(a, b):
    return a+b

def funcao(x):
    return 3 * x + 1


print(funcao(4))

"""


# Expressão Lambda
lambda x: 3 * x + 1


# E como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))


# Podemos ter Expressões lambdas com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()

print(nome_completo('angelina ', 'JOLIE'))
print(nome_completo('   FELICITY', 'JoneS'))


# Em funções Python, podemos ter nenhuma ou várias entradas. Lambdas também
amar = lambda: 'Como não amar Python?'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1/x + 1/y + 1/z)
# n = lambda x1, x2, ..., xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print((tres(3, 6, 9)))
# OBS: Se passarmos mais argumentos do que parâmetros esperados, teremos TypeError


# Outro Exemplo: Ordenando uma lista de por ordem alfabetica de sobrenomes
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C Clarke',
           'Frank Herbert', 'Orson Scott Card', 'Douglas Adams', 'H.G. Wells', 'Leigh Brackett']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


# Função Quadrática
# f(x) = ax^2 + bx + c

# Definindo a função
def geradora_funcao_quadratica(a, b, c):
    return lambda x: a*x**2 + b*x + c


teste = geradora_funcao_quadratica(1, 1, 1)
print(teste(0))
print(teste(1))
print(teste(2))

# OU:
print(geradora_funcao_quadratica(1, 1, 1)(1))




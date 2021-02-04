"""
Funções com Parâmetro Padrão (Default Parametres)
- Funções onde a passagem de parâmetro seja opcional;
    print('Drop the Beat')
    print()
- Funções onde a passagem de parâmetro não é opcional;
    def quadrado(numero):
    return numero ** 2

    print(quadrado(3))
    print(quadrado())  # TypeError - o parâmetro é obrigatório


#  Exemplo 1:
def exponencial(numero, potencia=2):  # Quando eu defino potencia padrão=2, ele se torna opcional
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # Por padrão, eleve ao quadrado
print(exponencial(3, 5))  # Eleva à potência informada pelo usuário


# OBS: Se o usuário passar apenas 1 parâmetro, este será atribuído apenas ao primeiro
# OBS: Se o usuário passar 2 argumentos, eles serão entendidos respectivamente

# OBS: Em funções Python, os parâmetros com valores default, DEVEM sempre estar ao final da declaração
# ERRO!
def teste(num=2, potencia):
    return num ** potencia

# Outros exemplos de erro:
def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))
print(soma(4))
print(soma())

# Outros Exemplos:
def mostra_informacao(nome='Drop', instrutor=False):
    if nome == 'Drop' and instrutor is True:
        return 'Bem-vindo instrutor Drop'
    elif nome == 'Drop':
        return 'Eu pensei que você era instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Nier'))

# Porquê utilizar parâmetros com valor default?
# Nos permite ser mais flexíveis nas funções:
# Evita erros com parâmetros incorretos
# Nos permite trabalhar com exemplos mais legíveis de código

# Quais tipos de dados podemos utilizar como valores default?
# Qualquer tipo de dado: Números, strings, floats, booleanos, listas, tuplas, dicionários, funções etc....


# Utilizando uma função dentro de outra:
def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo: Evitar problemas e confusões....
# Variáveis Globais
# Variáveis Locais
instrutor = "Drop"  # Variável Global


def diz_oi():
    instrutor = "Python"  # A varíavel Local se sobrepõe à global
    return f'Oi {instrutor}'


print(diz_oi())

# ATENÇÃO com variáveis globais: Se puder, evite!
total = 0

def incrementa():
    total = total + 1
    return total


print(incrementa())

# ATENÇÃO com variáveis globais: Se puder, evite!
total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1
    return total


print(incrementa())
"""


# Podemos ter funções que são declaradas dentro de funções e também têm uma forma especial de escopo
def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador += 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
print(dentro())  #NameError









"""
Entendendo o *args
1. O *args é um parâmetro como outro qualquer. Isso significa que pode
    assumir qualquer nome, desde que comece com asterico (*).
    Exemplo:
        *xis
        *ipsolon
2. O parâmetro *args utilizado em uma função coloca os valores extras
    informados como entrada em uma tupla. Lembrando que tuplas são imutáveis
    Exemplo Ruim:
    def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


    print(soma_todos_numeros(4, 6, 9))
    print(soma_todos_numeros(4, 6))  # TypeError: a função espera 3 parâmetros, enviamos 2
    print(soma_todos_numeros(4, 6, 7, 8))  # TypeError: a função espera 3 parâmetros, enviamos 4

    Exemplo Bom:
    def soma_todos_valores(*args):
    return sum(args)


    print(soma_todos_valores())
    print(soma_todos_valores(1))
    print(soma_todos_valores(2, 3))
    print(soma_todos_valores(2, 3, 4))

    # Exemplo Bom 2:
    def soma_todos_valores(nome, email, *args):
    return sum(args)


    print(soma_todos_valores('Dennys', 'Rodrigues', 1, 2, 3))

    # Exemplo Bom 3:
    def verifica_info(*args):
        if 'Drop' in args and 'the beat' in args:
            return 'Bem vindo Drop!'
        return 'Eu não tenho certeza de quem é você'


    print(verifica_info())
    print(verifica_info(1, True, 'Drop', 'the beat'))
"""


def soma_todos_valores(*args):
    return sum(args)


print(soma_todos_valores())
print(soma_todos_valores(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]


# Desempacotador
print(soma_todos_valores(*numeros))
# O Asterisco serve para informar o Python que estamos passando uma coleção de dados,
# desta forma, ele entende que precisa desempacotar os dados antes


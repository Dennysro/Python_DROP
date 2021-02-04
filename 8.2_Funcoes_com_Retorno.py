"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retorno de print: {ret_pr}')


OBS: Quando uma função não retorna nenhum valor, o retorno é "None"
OBS: Funções Python que retornam valores devem retornar estes valores com a palavra
     reservada "return"
OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma
     função. Podemos passar a execução da função para outras funções

# Exemplo de função
def quadrado_de_7():
    print(7 * 7)


ret = quadrado_de_7()
print(f'Retorno {ret}')


# Vamos refatorar esta função para que ela retorne o valor
def quadrado_de_8():
    return 8 * 8


ret8 = quadrado_de_8()  # Criamos uma variável para receber o retorno da função
print(f'Retorno: {ret8}')
print(f'Retorno: {quadrado_de_8()}')  # Mesmo resultado com 1 linha apenas


# Dois tipos diferentes de fatoração:
# Tipo 1:
def diz_oi():
    return "Oi "


print(diz_oi())
alguem = 'Pedro!'
print(diz_oi() + alguem)  # O Return da maior flexibilidade de uso para o dado de retorno


# Tipo 2:
def diz_oi2():
    print('Oi!')


diz_oi2()
print('Pedro')


OBS: Sobre a palavra reservada return:
    - Ela finaliza a função, ou seja, ela sai da execução da função.
    - Podemos ter em uma função diferentes returns
    - Podemos retornar qualquer tipo de dado e até mesmo multiplos valores

# Exemplo 1: Return finalizando a execução da função
def diz_oi():
    print('Estou sendo executado antes do retorno')
    return 'Oi! '
    print('Estou sendo executado após o retorno...')


print(diz_oi())


# Exemplo 2: Podemos ter diferentes returns em uma função
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


# Exemplo 3: Podemos em uma função, retornar qqr tipo de dado e até mesmo multiplos valores
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)


# Vamos criar uma função para simular uma moeda
import random


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random.choice([0, 1]) == 1:
        return "Cara!"
    return "Coroa!"


print(joga_moeda())


# Erros comuns na utilização do retorno (Codificação desnecessária)
def eh_impar():
    numero = 6
    if numero % 2 != 0:
        return True
    else:                    # Linha desnecessária > Evitar
        return False


print(eh_impar())

"""

# Vamos criar uma função para simular uma moeda
import random


def joga_moeda():
    # Gera um número pseudo-randômico entre 0 e 1
    if random.choice([0, 1]) == 1:
        return "Cara!"
    return "Coroa!"


print(joga_moeda())


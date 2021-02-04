"""
Funções com Parâmetros (de entrada)
    - Funções que recebem dados para serem processados dentro da mesma

Se pensarmos em um programa qualquer, geralmente temos:
    entrada -> processamento -> saída
Se pensarmos em uma função, já sabemos que temos funções que:
    - Não possuem entrada
    - Não possuem saída
    - Possuem entrada mas não possúi saída
    - Não possuem entrada mas possuem saída
    - Possuem entrada e saída

# Função que recebe um parâmetro
def quadrado(numero):
    return numero * numero
    # Ou return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)


# Refatorando a função
def cantar_parabens(aniversariante):
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}')


cantar_parabens("Dennys")


# Funções podem ter n parâmetros de entrada. Apenas separar os parâmetros por vírgula
# Exemplo
def soma_n1_n2(n1, n2):
    return n1 + n2


def multiplica_n1_n2(n1, n2):
    return n1 * n2


def outra(n1, n2, msg):
    return (n1 + n2) * msg


print(soma_n1_n2(2, 5))
print(multiplica_n1_n2(2, 5))
print(outra(3, 2, "Drop"))


# OBS: Se informarmos um número errado de parâmetros, teremos TypeError


# Nomeando Parâmetros
def nome_completo(string1, string2):
    return f'Seu nome completo é {string1} {string2}'


# É melhor:
def nome_completo(nome, sobrenome):  # Parametros nome e sobrenome
    return f'Seu nome completo é {nome} {sobrenome}'


# Diferença entre Parâmetros e Argumentos
# Parâmetros são variáveis declaradas na definição de uma função
# Argumentos são dados passados durante a execução de uma função


print(nome_completo("Dennys", "Rodrigues"))  # Argumentos Dennys Rodrigues

# Argumentos nomeados (Keyword arguments)
# Caso utilizemos nomes dos parâmetros nos arugmentos para informá-los, podemos
# utilizar qualquer ordem

print(nome_completo(nome="Cleisson", sobrenome="Silva"))
print(nome_completo(nome="Silva", sobrenome="Cleisson"))

"""


# Return tem que estar na identação da definição da função:
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))




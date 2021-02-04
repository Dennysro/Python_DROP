"""
Loop for
Loop -> Uma estrutura de repetição.
For  -> Uma dessas estruturas

C ou Java:
for(int i=0; i<10; i++){
    //execução do loop
}

Python
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
    -String
        nome = 'Drop'
    -Lista
        lista = {1, 3, 5, 7, 9}
    -Range
        números = range(1, 10)
"""
'''
nome = 'Drop the beat'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando sobre uma String):
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range - OBS: Valor final não está incluso na iteração)
for numero in range(1, 10):
    print(numero)

# Seguindo... (Enumerate: ((0, 'D'), (1, 'r'), (2, 'o'), (3, 'p'), ...)
# Enumerate mostra/cria um índice para cada parte de uma lista
for indice, letra in enumerate(nome):
    print(letra)

# Ou:
for _, letra in enumerate(nome):
    print(letra)

# Ou:
for valor in enumerate(nome):
    print(valor, end='')  # o end='' faz com que ele não pule a linha para exibir

->Tabela de emojis: https://apps.timwhitlock.info/emoji/tables.unicode 

'''
# Seguindo um pouco mais a fundo:

qtd = int(input('Quantos valores você quer somar?'))  # Quantas vezes esse loop deve rodar?
soma = 0
for n in range(1, qtd+1):  # qtd+1 porque o range n pega a ultima lembra?
    num = int(input(f'Informe o {n}º valor: '))
    soma = soma + num
print(f'A soma dos {n} valores é {soma}')

'''
# Original: U+1F60D
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 4):
        print('\U0001F60D' * num)
'''


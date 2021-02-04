"""
Listas (list)

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens,
com a diferença de serem DINÂMICAS e também de podermos colocar QUALQUER tipo de
dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo. Ou seja se criarmos um array do tipo int,
    e com tamanho 5, este array será SEMPRE deste tipo e tamanho

Linguagem em Python:
    - Dinâmico. Não possuem tamanho fixo; é possivel criar uma lista e ir adicionando
    elementos.
    - Qualquer tipo de dado. Não possuem tipo de dado fixo, ou seja aceitam qualquer
    tipo de dado

As listas em Python são representadas por colchetes: []
"""
"""
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['D', 'r', 'o', 'p']
lista3 = []
lista4 = list(range(11))
lista5 = list('Drop')

# Podemos checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o valor {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('o'))
"""
"""
É possivel adicionar elementos em listas também (append):

# Só é possível adicionar um elemento por vez (lista1.append(1, 2, 3) da erro
print(lista1)
lista1.append(42)
print(lista1)

# Se usarmos um elemento do tipo lista, é possível adicionar mais de um elemento:
lista1.append([1, 2, 3])
print(lista1)
if [1, 2, 3] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

# Para colocar diferentes elementos como elementos individuais na lista, utilizamos:
# função list.extend
lista1.extend([123, 44, 67])
print(lista1)
lista1.extend('Drop')
print(lista1)

# Podemos inserir um novo elemento na lista informando a posiçãp do índice:
# O novo valor não substitui o valor existente, apenas desloca tudo pra frente
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos juntar duas listas:
lista6 = lista1 + lista2
print(lista6)
# Ou:
lista1 += lista2
print(lista1)
# Ou:
lista1.extend(lista2)
print(lista1)

# É possível inverter a ordem dos valores de uma lista:
lista1.reverse()
print(lista1)
# Ou, podemos usar o Slice:
print(lista1[::-1])
print(lista2[::-1])

# Podemos copiar uma lista:
lista6 = lista2.copy()
print(lista6)

# Para contar quantos elementos existem em uma lista: len()
print(len(lista3))
print(len(lista4))

# Podemos também remover o último elemento de uma lista: pop()
# o list.pop() não somente remove o último elemento, mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Para remover um elemento pelo seu índice;
# Os elementos à direita do índice serão deslocados para esquerda
# Se não houver elemento no índice informado, teremos IndexError
print(lista5)
lista5.pop(0)
print(lista5)

# Podemos remover todos os elementos de uma lista:
print(lista1)
lista1.clear()
print(lista1)

# Podemos repetir elementos de uma lista:
nova = [1, 2, 3]
nova *= 3
print(nova)

# Podemos converter strings em listas:
# Por padrão, o split() separa elementos quando identifica o espaço ' '
curso = 'Programação em Python Essencial'
curso = curso.split()
print(curso)

# Exemplo 2:
curso = 'Programação,em,Python,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string:
# Pega a lista 6, pega cada elemento, adiciona um espaço entre os elementos
# e transforme em uma String
lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)
curso = ' '.join(lista6)
print(curso)

# Outra forma: (Colocando $ entre os elementos)
curso = '$'.join(lista6)
print(curso)

"""
# ________________________________________________________________________
"""# Iterando sobre listas:
# Exemplo 1: Utilizando for
lista8 = list('Drop the Beat')
print(lista8)
for elemento in lista8:
    print(elemento)

# Exemplo 2: Utilizando while
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
"""

# __________________________________________________________________________
"""
# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
numeros = [n1, n2, n3, n4, n5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada:
cores = ['Verde', 'Amarelo', 'Azul', 'Branco']
print(cores[0])  # Verde
print(cores[1])  # Amarelo
print(cores[2])  # Azul
print(cores[3])  # Branco

# Fazendo acesso aos elementos de forma indexada inversa:
print(cores[-1])  # Branco
print(cores[-2])  # Azul
print(cores[-3])  # Amarelo
print(cores[-4])  # Verde

print('')

for cor in cores:
    print(cor)

print('')

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar indice em um for:
for indice, cor in enumerate(cores):
    print(indice, cor)

print('')

# Relembrando função enumerate
teste = list(enumerate('Drop the Beat'))
print(teste)

# Outros métodos uteis:
# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]
# Em qual índice estão os valores 6 e 9?
print(numeros.index(6))
print(numeros.index(9))

# Caso não exista o elemento na lista, será apresentado Erro
# Caso o valor se repita na lista, a função index retornará apenas o índice da 1a ocorrencia

# Podemos fazer busca dentro de um range, qual índice começar a buscar
print(numeros.index(5, 2))  # 'A partir da posição 2...'

# Podemos fazer busca dentro de um range definido
print(numeros.index(8, 3, 6))  # 'A partir da posição 3 até a 6...'

# Revisão de slicing
# lista[início:fim:passo]
# range(início:fim:passo)

# Trabalhando com o parâmetro 'inicio':
lista = [1, 2, 3, 4]
print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes

# Trabalhando com o parâmentro 'fim':
print(lista[:2])  # Inicia em 0, e vai até índice 2 (não incluso o 2)

# Trabalhando com ambos parâmetros 'início' e 'fim':
print(lista[1:3])

# Trabalhando com o parâmetro 'passo':
print(lista[0::2])
print(lista[0::-1])

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho:
# *Se todos forem inteiros ou reais

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# Transformar lista em tupla:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas:
lista = [1, 2, 3]
n1, n2, n3 = lista
print(n1)
print(n2)
print(n3)
# Se houverem mais elementos para desempacotar do que variaveis para receber os dados,
# ou vice versa, teremos ValueError

# Copiando uma lista para outra (Shallow copy e Deep Copy)
# Deep Copy: As modificações na lista copiada não afetam a original (Independentes)
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)

print(lista)
print(nova)

# Shallow Copy: As modificações na lista nova são carregadas à lista original. (Dependentes)
lista = [1, 2, 3]
print(lista)

nova = lista  # Cópia

print(nova)
nova.append(4)

print(lista)
print(nova)
"""

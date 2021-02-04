"""
Conjuntos:
    1. Conjuntos em qualquer linguagem de programação,
    fazem referência à teoria dos conjuntos da matemática
    2. No Python os conjuntos são chamados de Sets.
    3. Da mesma forma que na matematica, os Sets não possuem
    valores duplicados, não possuem valores ordenados, e elementos
    não são acessados via ìndice. (Conjuntos não são indexados)
    4. Conjuntos são ótimos para se utilizar quando precisamos armazenar
    elementos mas não nos importamos com ordenação deles nem com chave/itens
    duplicados.
    5. Conjuntos (sets) são referenciados em Python com chaves {}*
    * A diferença entre Sets e Dicionários: Um dicionário tem chave/valor e
    um conjunto têm apenas valor

# Definindo um conjunto:
# Forma 1: As repetições não são adicionadas ao conjunto... São ignoradas sem gerar Erros
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)
print(type(s))

# Forma 2: Mais comum (Também ignora repetições do set)
s = {1, 2, 3, 4, 5, 5, 6, 7}
print(s)
print(type(s))

# Verificando se está no conjunto, normal...
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem
# Comparações entre as coleções

# Listas aceitam valores duplicados, logo temos 9 elementos
lista = [99, 2, 2, 34, 34, 12, 1, 44, 5]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, logo temos 9 elementos
tupla = 99, 2, 2, 34, 34, 12, 1, 44, 5
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, logo temos 7 elementos
dicionario = {}.fromkeys(lista, 'Dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, logo temos 7 elementos.
# A Ordem dos elementos também não importa
conjunto = {99, 2, 2, 34, 34, 12, 1, 44, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets
s = {1, 'b', True, 34.56, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes dos Sets:
# Imagine que fizemos um formulário de cadastro de visitantes em um feira.
# Os visitantes informam manualmente a cidade de onde vieram.
# Nós adicionamos cada cidade em uma lista Python, já que ela aceita +elementos e repetição
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Precisamos saber quantas cidades distintas existem, podemos usat o set!
print(len(set(cidades)))

# Adicionando elementos em um conjunto:
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidades não geram erros, apenas são ignoradas
print(s)

# Remover elementos em um conjunto:
# Forma 1: Nenhum valor é retornado
s = {1, 2, 3}
print(s)
s.remove(3)  # Não é índice! É o valor a ser removido, conjuntos não são indexados!
# s.remove(33)  # Caso valor não seja encontrado: KeyError
print(s)

# Forma 2:
s.discard(2)
print(s)
s.discard(22)  # Caso o valor não seja encontrado, não é gerado erro

# Copiando um conjunto para outro...
# Deep Copy:
s = {1, 2, 3}
novo = s.copy()
novo.add(4)

print(s)
print(novo)

# Shallow Copy:
novo = s
novo.add(4)
print(s)
print(novo)

# Podemos remover todos elementos:
s.clear()
print(s)
"""

# Métodos matematicos de Conjuntos:
# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python
# e um contendo estudantes do curso Java.
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
# Veja que alguns alunos que estudam Python também estudam Java.


# Precisamos gerar um conjunto com nomes de estudantes únicos
# Forma 1: Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2: Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)


# Precisamos gerar um conjunto de estudantes que estão em ambos os grupos:
# Forma 1: Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2: Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Gerar um conjunto de estudantes de um curso, que não estão no outro:
so_python = estudantes_python.difference(estudantes_java)
print(so_python)
# Ou
so_java = estudantes_java.difference(estudantes_python)
print(so_java)


# Soma, Valor Máximo, Valor Mínimo, Tamanho*
# Somente para valores reais ou inteiros..
s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))









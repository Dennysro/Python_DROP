"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas. Existindo basicamente 2 diferenças:
    1. Tuplas são representadas por parêntesis ()
    2. As Tuplas são imutáveis. Ao se criar uma tupla, ela não muda.
        Toda operação sobre uma tupla gera umanova tupla.

# CUIDADO 1: As tuplas são representadas por parêntesis (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(()))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento - Tuplas são definidas pela vírgula e não ()
tupla3 = (4)  # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 5,  # Isso é uma tupla
print(tupla5)
print(type(tupla5))

# Criando uma tupla a partir de um range (Dinâmicamente)
tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tuplas:
tupla = ('Drop the Beat', 'Right Now')
n1, n2 = tupla
print(n1)
print(n2)

# Métodos para adição e remoção de elementos nas tuplas são inexistentes, por serem imutáveis
# Soma, Valor Máximo, Valor Mínimo, Tamanho => Para inteiros ou reais
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(min(tupla))
print(max(tupla))
print(len(tupla))

# Concatenação de tuplas:
tupla1 = 1, 2, 3
print(tupla1)

tupla2 = 4, 5, 6
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutáveis

tupla1 += tupla2  # É possível sobrescrever os valores
print(tupla1)

# Verificações dentro de tuplas
tupla = 1, 2, 3
print(3 in tupla)

# Iterando sobre tuplas:
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla:

tupla = ('a', 'b', 'c', 'd', 'a', 'b', 'f')
print(tupla.count('c'))

escola = tuple('Drop the beat')
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas:
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1: Meses

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# Exemplo 2: Acesso a elementos de uma tupla é semelhante à listas.
print(meses[5])

# Iterar com while:
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificar qual índice de um elemento da tupla:
print(meses.index('Junho'))  # Caso o elemento não exista, será gerado Erro

# Slicing: Tupla[início, fim, passo]
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses[0:])

# Copiando Tuplas:
tupla = (1, 2, 3)
print(tupla)
nova = tupla
print(nova)
print(tupla)


# Por quê usar Tuplas?
# Tuplas são mais rápidas do que listas.
# Tuplas deixam seu código mais seguro. (Imutabilidade)

"""

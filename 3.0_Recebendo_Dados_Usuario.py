"""
Recebendo dados do usuário

input() -> Todo dado recebido do tipo input é do tipo STRING

Em python, STRING é tudo que estiver entre:
    -Aspas simples
    -Aspas duplas
    -Aspas simples triplas
    -Aspas duplas triplas
"""

# Entrada de Dados (input)
#print("Qual seu nome?")
#nome = input()

nome = input('Qual seu nome?')

# Exemplo de print 'Antigasso':
# print("Seja bem-vindo(a) %s" % (nome))
# Exemplo de print 'Antigo':
#print('Seja bem-vindo(a) {0}' .format(nome))

# Exemplo de print 'Moderno':
print(f'Seja bem-vindo(a) {nome}')
#print("Qual sua idade?")
#idade = input()

idade = int(input('E qual sua idade?'))

# Saída
# Exemplo de print 'Antigasso' 2:
# print("O usuário %s tem %s anos" % (nome, idade))
# Exemplo de print 'Antigo' 2:
#print('O usuário {0} tem {1} anos' .format(nome, idade))

# Exemplo de print 'Moderno':
print(f'O usuário {nome} têm {idade} anos')
print(f'E digo mais, {nome} nasceu em {2020 - idade}!')

"""
Para trocar o tipo de variável
int(idade) => cast
"""


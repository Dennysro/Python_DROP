"""
Estruturas lógicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not,
Operadores binários:
    - and, or, is

Para 'and', ambos valores precisam ser True
Para 'or', apenas um dos valores precisa ser True
Para 'not', o valor do booleano é invertido, ou seja, se for True vira False e vice-versa
Para 'is', o valor é comparado com um segundo
"""

ativo = True
logado = False

if ativo and logado:
    print('Bem-vindo Usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu email!')

if ativo or logado:
    print('Bem-vindo Usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu email!')

if not ativo:
    print('Bem-vindo Usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu email!')

if ativo is False:
    print('Bem-vindo Usuário')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu email!')


"""
**kwargs (**xis, **whatever, assume qualquer nome antecedido por 2 asteriscos)

Este é só mais um parâmetro, porém diferente do *args, que coloca os valores extras
 em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados e transforma esses
 parâmetros extras em um dicionário.


# Exemplo:
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor.title()}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')
# OBS: Nem os parâmetros *args e **kwargs são obrigatórios:
cores_favoritas(drop='vermelho')

# Exemplo mais complexo:

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossa funções podemos ter (NESTA ordem):
# 1. Parâmetros obrigatórios
# 2. *args
# 3. Parâmetros default
# 4. **kwargs

# Exemplo:


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, "Carla", 9, 4, 3, java=False, python=True)

# Entenda porque é importante manter a ordem dos parâmetros na declaração:
# Ordem correta:
def mostra_info(a, b, *args, instrutor="Drop", **kwargs):
    return [a, b, args, instrutor, kwargs]


# Da forma que está escrito aqui o que deverá acontecer:
# a = 1
# b = 2
# args = (3,)
# instrutor = 'Drop'
# kwargs = {'sobrenome': 'Rod', 'cargo': 'Piloto')
print(mostra_info(1, 2, 3, sobrenome='Rod', cargo='Piloto'))


# Ordem incorreta:
def mostra_info(a, b, instrutor="Drop", *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


# Da forma que está escrito aqui o que deveria acontecer, mas não acontece:
# a = 1
# b = 2
# args = (3,)
# instrutor = 'Drop'
# kwargs = {'sobrenome': 'Rod', 'cargo': 'Piloto')
print(mostra_info(1, 2, 3, sobrenome='Rod', cargo='Piloto'))

# Desempacotar com o **kwargs:
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))
"""


def soma_multiplos_num(a, b, c, **kwargs):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)

soma_multiplos_num(*lista)
soma_multiplos_num(*tupla)
soma_multiplos_num(*conjunto)
soma_multiplos_num(**dicionario)  # Os nomes das chave do dic. devem ser os mesmos dos parâmetros da função

soma_multiplos_num(**dicionario, lang='Python')


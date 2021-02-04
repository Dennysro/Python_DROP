"""
Estruturas condicionais
if, else, elif

"""

nome = input('Qual seu nome?')
idade = int(input(f'Prazer {nome}, e qual a sua idade?'))

if idade < 18:
    print("Menor de Idade")
    print(f'Você só têm {idade} anos!')
elif idade == 18:
    print(f'O usuário {nome} têm 18 anos')
elif idade == 25:
    print('Acertou miseravi')
else:
    print(f'Pode entrar {nome}, você é maior de idade')


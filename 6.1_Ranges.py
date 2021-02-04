"""
Ranges
- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:
1- range(valor_de_parada)
    OBS: valor_de_parada não inclusive (Início padrão 0, e passo de 1 em 1)

2- range(valor_de_inicio, valor_de_parada)
    OBS: valor_de_parada não inclusive (Início especificado pelo usuário, e passo de 1 em 1)

3- range range(valor_de_inicio, valor_de_parada, passo)
    OBS: valor_de_parada não inclusive (Início especificado pelo usuario, e passo especificado pelo usuário)

4- range(valor_de_início, valor_de_parada, passo)
    OBS: valor_de_inicio não inclusive (Início especificado pelo usuario, e passo especificado pelo usuário)
    OBS: É decremental, subtrai um

BÔNUS:
lista = list(range(10)) 'Retorna:'
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

"""

# Forma 1 (Começando do 0 padrão)
for num in range(11):
    print(num)

# Forma 2 range(valor_de_inicio, valor_de_parada não incluso)
for num in range(3, 11):
    print(num)

# Forma 3 range(valor_de_inicio, valor_de_parada, passo)
for num in range(1, 10, 2):
    print(num)

# Forma 4 range(valor_de_final, valor_de_parada, passo)
for num in range(10, 0, -1):
    print(num)

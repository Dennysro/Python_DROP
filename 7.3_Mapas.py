"""
Mapas:
    1. Em Python são conhecidos como dicionários
    2. São representados por chaves


"""

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

# Obtendo as chaves apenas:
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Obtendo os valores:
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários:
print(receita.items())

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# Soma, Valor Maximo, Valor Minimo, Tamanho:
# Se valores forem todos inteiros ou reais

print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))

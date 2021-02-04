"""
Dicionários:
    1. Em algumas linguagens de programação, os dicionários Python são conhecidos
    por 'mapas'
    2. São coleções do tipo chave/valor.
    3. São representados por chaves {}. -> print(type({}))
    4. As chaves ou valores podem ser de qualquer tipo
    5. Chaves e Valores são separados por 'Dois pontos' (chave:valor)

# Forma 1: Mais comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2: Menos comum:
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

# Acessando elementos:
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Forma 1: Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])  # Dicionários não são indexados, logo para acessar é preciso usar a chave
print(paises['py'])
# print(paises['ru']) # Casos tentamos acessar algo que não exista, ocorrerá KeyError

# Forma 2: Recomendada - acessando via get
print(paises.get('br'))
print(paises.get('py'))
# print(paises.get('ru')) # Aqui  não da o KeyError, o programa retorna o valor 'None'

# Sabendo que o tipo 'None' é sempre False
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('ru')

if pais:  # Mesma coisa que 'if True'
    print(f'Encontrei o país {pais}')
else:
    print(f'Não encontrei o país')

# Podemos definir um valor padrão para caso não encontremos o objeto/valor com a chave informada
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('ru', 'Não Encontrado')  # Caso o get não encontre a chave 'ru' será retornado o valor após a virgula
print(f'{pais}')

# Buscando informações dentro do dicionário. A busca é sempre pela chave!
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
print('br' in paises)
print('eua' in paises)
print('Estados Unidos' in paises)
print('ru' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Utilizando diferentes tipos de dados como chaves dentro de um dicionário:
# Tuplas como chave são uma boa pratica, por serem imutáveis.
localidades = {
    (35.567, 39.768): 'Escritório em Londres',
    (56.789, 23.456): 'Escritório em New York',
    (78.909, 123.456): 'Escritório em Xangai',
}

print(localidades)
print(type(localidades))

# Adicionando elementos em dicionários.
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1: Mais comum
receita['abr'] = 358
print(receita)
print(type(receita))

# Forma 2:
novo_dado = {'mai': 500}
receita.update(novo_dado)  # É a mesma coisa que: receita.update({'mai': 500})
print(receita)
print(type(receita))

# Atualizando dados em um dicionário:
# Forma 1:
receita['mai'] = 550
print(receita)

# Forma 2:
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar ou modificar elementos em um dict é a mesma
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário:
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
# Forma 1: o pop para dicionários exige a informação da chave. Caso não encontre: KeyError
ret = receita.pop('mar')
print(ret)
print(receita)

# Forma 2: Utilizando a função del. Caso não encontre: KeyError
del receita['fev']
print(receita)

# Imagine que você tem um comércio eletrônico, onde temos um carrinho virtual:

Carrinho de compras:
    Produto 1:
        - nome
        - quantidade
        - preço
    Produto 2:
        - nome
        - quantidade
        - preço

# 1 - Poderiamos utilizar uma lista para isso? Sim!
carrinho = []

produto1 = ['Plastation 4', 1, 1999.00]
produto2 = ['God of War 4', 1, 159.99]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Problema: Teríamos que saber qua o índice de cada informação no produto

# 2 - Poderíamos utilizar uma tupla para isso? Sim!

produto1 = ('Playstation 4', 1, 1999.00)
produto2 = ('God of War 4', 2, 159.99)

carrinho = (produto1, produto2)

print(carrinho)
# Problema: Teríamos que saber qua o índice de cada informação no produto

# 3 -  Poderíamos utilizar um dicionário para isso? Sim!

carrinho = []

produto1 = {'nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 1999.00}
produto2 = {'nome': 'God of War 4', 'Quantidade': 1, 'Preço': 159.99}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Aqui temos os índices de cada informação

# Limpar o dicionário (Zerar dados)
d.clear()
print(d)

# Mais métodos de dicionários:
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Copiando dicionários:
# Forma 1: Deep Copy
novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma 2: Shallow Copy
novo = d
print(novo)

novo['e'] = 5
print(d)
print(novo)
"""

# Forma não usual de criação de dicionários:
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['Nome', 'Pontos', 'Email', 'Profile'], 'Desconhecido')
print(usuario)
print(type(usuario))

# O método .fromkeys recebe dois valores: um interável e um valor
# Ele irá gerar para cada valor do iterável uma chave e irá atribuir a esta chave, o valor informado

veja = {}.fromkeys('Teste', 'Valor')
print(veja)
# Exemplo curioso: Variáveis string são iteráveis, e não existem chaves repetidas!

# Outro exemplo utilizando range:
veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)


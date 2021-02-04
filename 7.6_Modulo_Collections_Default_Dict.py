"""
Módulo Collections - High-performance Container Datatypes

Default Dict (Dicionário Padrão):
    1. Não apresenta o KeyError em caso de não haver correspondência
    de valor para a chave informada
    2. Ao criar um Default Dict, nós informamos um valor default, podendo
    usar um lambda para isso. Este valor será utilizado sempre que não
    houver um valor definido para a chave informada.
    3. Caso tentemos acessar uma chave inexistente, essa chave será criada,
    e o valor default será atribuído.
    4. 'lambdas' são funções sem nomes que podem ou não receber parâmetros de
    entrada e retornar valores

# Relembrando sobre dicionários:
dicionario = {'Curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['Curso'])

"""

# Fazendo o import
from collections import defaultdict

# Criando o dicionário
dicionario = defaultdict(lambda: 0)
dicionario['Curso'] = 'Programação em Python: Essencial'

# Testando o valor default
print(dicionario['Outro'])  # KeyError no dicionario comum, mas aqui não
print(dicionario)


"""
PEP8 - Python Enchacement Proposal
The Zen of Python
import this
A ideia da pep8 é que possamos escrever códigos Python de forma Pythônica(Elegante)

1- UTILIZE CAMEL CASE PARA NOMES DE CLASSES

class Calculadora
    pass

class DennysRodrigues
    pass


2- UTILIZE NOMES EM MINÚSCULO, SEPARADOS POR UNDERLINE PARA FUNÇÕES OU VARIÁVEIS

def soma()
    pass

def soma_dois()
    pass

numero_impar = 5


3- UTILIZE 4 ESPAÇOES PARA IDENTAÇÃO!(OBS: TAB pode dar errado dependendo do tamanho configurado do tab)

if 'a' in 'banana':
    print('tem')

4- LINHAS EM BRANCO
    -Duas linhas em branco entre definições de classe e funções sempre;
    -Métodos dentro de uma classe devem ser separados com uma única linha em branco;


5- SOBRE IMPORTS
    -Imports devem sempre ser feitos em linhas separadas;

# Import Errado
import sys, os

# Import Certo
import sys
import os

# Não há problemas em utilizar:
from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo logo depois de quaisquer comentários ou docstrings e antes de
# constantes ou variáveis globais


6- ESPAÇOS EM EXPRESSÕES E INSTRUÇÕES

# NÃO FAÇA:
funcao( algo[ 1 ], { outro: 2 } )
algo (1)
dict ['chave'] = lista [indice]
x              = 1
y              = 2
variavel_longa = 3


# FAÇA:
funcao(algo[1], [outro: 2])
algo(1)
dict['chave'] = lista[indice]
x = 1
y = 2
variavel_longa = 5

7- TERMINE SEMPRE UMA INSTRUÇÃO OU CÓDIGO COM UMA NOVA LINHA
"""
import this

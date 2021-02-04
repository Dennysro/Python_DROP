"""
Módulo Collections - High-performance Container Datatypes

Counter (Contador):
        1. Recebe um Iterável como parâmetro e cria um objeto do tipo
        Collections Counter que é parecido com um dicionário, contendo
        como chave o elemento da lista passada como parâmetro e como
        valor a quantidade de ocorrências desse elemento

# Exemplo 1:
# Realizando o import
from collections import Counter

# Poderia ser qualquer Iterável, aqui usamos lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)
# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 66: 2, 45: 1, 43: 1, 34: 1})
# Para cada elemento da lista, o Counter criou uma chave e colocou como valor a qtd de ocorrências

# Exemplo 2:
from collections import Counter

print(Counter('Drop the Beat'))
# Counter({' ': 2, 't': 2, 'e': 2, 'D': 1, 'r': 1, 'o': 1, 'p': 1, 'h': 1, 'B': 1, 'a': 1})

"""

# Exemplo 3:

from collections import Counter

texto = """
Soneto XVII

No te amo como se fueras rosa de sal, topacio
o flecha de claveles que propagan el fuego:
te amo como se aman ciertas cosas oscuras,
secretamente, entre la sombra y el alma.

Te amo como la planta que no florece y lleva
dentro de sí, escondida, la luz de aquellas flores,
y gracias a tu amor vive oscuro en mi cuerpo
el apretado aroma que ascendió de la tierra.

Te amo sin saber cómo, ni cuándo, ni de dónde,
te amo directamente sin problemas ni orgullo:
así te amo porque no sé amar de otra manera,

sino así de este modo en que no soy ni eres,
tan cerca que tu mano sobre mi pecho es mía,
tan cerca que se cierran tu ojos con mi sueño.
"""
palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontra as 5 palavras de maior ocorrência:
print(res.most_common(5))


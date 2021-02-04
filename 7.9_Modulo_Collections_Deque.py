"""
Módulo Collections - High-performance Container Datatypes

Deque (Lista de alta performance)
"""

# Fazendo o import
from collections import deque

# Criando o deque
deq = deque('Dommys')
print(deq)

# Adicionando elementos no deque
deq.append('s')
print(deq)

deq.appendleft('D')
print(deq)

# Removendo elementos no deque
print(deq.pop())
print(deq)
print(deq.popleft())
print(deq)



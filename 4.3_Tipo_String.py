"""
Tipo String
Em Pyhton, um dado é considerado do tipo string sempre que:
-Estiver entre aspas simples: ('String', '235', 'a', 'True', '42.3')
-Estiver entre aspas duplas: ("String", "235", "a", "True", "42.3")
-Estiver entre aspas simples triplas
-Estiver entre aspas duplas triplas

nome = 'Drop online'
print(nome)
print(type(nome))

nome = "Drop's Bar"
print(nome)
print(type(nome))

# Para pular uma linha:
nome = "Drop's \nBar"
print(nome)
print(type(nome))
"""

nome = "drop the beat"
print(nome.upper())
print(nome.lower())

print(nome.split())  # Separa/Transforma em uma lista de strings
# ['d', 'r', 'o', 'p', ' ', 't', 'h', 'e', ' ', 'b', 'e', 'a', 't']
# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12]
print(nome)
print(nome.split()[2])

print(nome[::-1])  # 'Comece do primeiro elemento, vá até o ultimo e inverta a string

print(nome.replace('b', 'm'))  # Substituindo elementos da string

texto = 'Socorram me subino onibus em marrocos'  #Palíndromo
print(texto)
print(texto[::-1])


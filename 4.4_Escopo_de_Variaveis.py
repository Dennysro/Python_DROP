"""
Escopo de variáveis
Dois casos de escopo:
1.Escopo das variáveis Globais
    -São reconhecidas, ou seja, seu escopo compreende todo o programa
2.Escopo das variáveis Locais
    -São reconhecidas apenas no bloco onde foram declaradas, ou seja,
    seu escopo está limitado ao bloco onde foi declarada

Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variável

Em Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 42
print(numero)
print(type(numero))

numero = "Drop"
print(numero)
print(type(numero))

nao_existo = 'Oi'
print(nao_existo)

numero = 2    # Variável numero é variável global

if numero > 10:
    novo = numero + 10    # Variável novo é variável local
    print(novo)

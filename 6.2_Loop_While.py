"""
Loop While

Forma geral:
while expresao_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira
Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso
Exemplo: nome = 5 >> num < 5 >> False


"""

# OBS: Em um loop while é importante que cuidemos do critério de parada
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1

# OBS 2:
resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou jessica?')


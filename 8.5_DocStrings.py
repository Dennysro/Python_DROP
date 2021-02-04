"""
Documentando funções com Docstrings
- Serve para deixar o código mais claro para que for ler.
- Podemos ter acesso à documentação de uma função em Python utilizando 2 formas:
    1. __doc__ como no exemplo:
      print(diz_oi.__doc__)
    2. print(help(diz_oi))


"""


def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'



print(diz_oi())
print(help(diz_oi))


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero', ou 'numero' à 'potencia' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potência que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencia'
    """
    return numero ** potencia


print(exponencial(2))
print(help(exponencial))

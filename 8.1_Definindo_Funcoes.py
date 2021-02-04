"""
Definindo Funções
    - Funções são pequenos trechos de código que realizam tarefas específicas.
    - Já utilizamos várias funções desde o início do curso.
        - print()
        - len()
        - max()
        - min()
        - ...
    - Pode ou não receber entradas de dados e retornar saída de dados
    - Muito úteis para executar procedimentos similares por repetidas vezes
    - OBS: Se escrevermos uma função que realiza várias tarefas dentro dela,
            é bom fazer uma verificação para que a função seja simplificada

"""
"""
# Exemplo de utilização de funções:
cores = ['verde', 'amarelo', 'azul', 'branco']
curso = 'Programação em Python Essencial'

# Utilizando a função integrada (Built-in) do Python print()
print(cores)
cores.append('roxo')  # Função .append()
print(cores)
cores.clear()  # Função .clear()
print(cores)

# Princípio DRY = Don't Repeat Yourself // Não repita seu código
"""
"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:
nome da funcao -> SEMPRE com letras minúsculas, e se composto, separado por underlines (Snake Case)
parametros_de_entrada -> Opcionais, caso exista mais de um, devem ser separados por vírgula
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento acontece
                    Pode ter retorno no bloco ou não

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def', informando ao Python que 
     estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos (:)
     que é utilizado em Python para definir blocos           
"""
"""

# Definindo uma função
def diz_oi():
    print('Oi')


# Utilizando a função, atenção em sempre utilizar o parêntesis
diz_oi()

"""
"""
OBS: 
1- Veja que dentro das funções podemos utilizar outras funções.
2- Veja que a função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi
3- Veja que a função não recebe nenhum parâmetro de entrada
4- Veja que esta função não retorna nada
"""


# Exemplo
def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')


for n in range(4):
    cantar_parabens()


# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função pela varíavel
canta = cantar_parabens
canta()
# Não é usual, e gera confusão, não é recomendado



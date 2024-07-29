# Funções

def soma(num1, num2): # definição de função soma
    calculo = num1 + num2
    print(f'Resultado da soma é: {calculo}')

def subtracao(num1, num2):
    sub = num1 - num2
    print(f'Resultado da subtração é: {sub}')

def multiplicacao(num1, num2):
    mult = num1 * num2
    file = 'arquivo.txt'

    # arquivos

    # abertura
    """arquivo_escrita = open(file, 'w') # Abertura para escrita
    arquivo_leitura = open(file, 'r') # Abertura somente para leiura
    arquivo_binario = open(file, 'wb') # Abertura de arquivos binários"""

    # escrita
    arquivo_escrita = open(file, 'w') # Abertura para escrita
    arquivo_escrita.write(f'Resultado da multiplicacao e: {mult}')
    arquivo_escrita.close()

    # leitura
    arquivo_leitura = open(file, 'r') # Abertura somente para leiura
    leitura = arquivo_leitura.read()
    arquivo_leitura.close()
    print(leitura)

def divisao(num1, num2):
    # exceções
    try:
        div = num1 / num2
        print(f'Resultado da divisão é: {div}')

    except ZeroDivisionError:
        print('Impossível dividir um valor por zero')
    except TypeError as e:
        print(f'Erro: O tipo do dado informado esta incorreto. \nDetalhes: {e}')  
    else:
        print('Cálculo realizado com sucesso')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

soma(num1, num2) # chamando a função
subtracao(num1, num2)
multiplicacao(num1, num2) # chamada de função dentro de uma função

divisao(10,0)
divisao(10, 'womakercode')
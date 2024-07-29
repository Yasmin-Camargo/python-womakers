'''
Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão
'''

def soma(num1, num2):
    resultado = num1 + num2
    print(f'\nSoma: {num1} + {num2} = {resultado}')

def subtracao(num1, num2):
    resultado = num1 - num2
    print(f'\nSubtração: \n{num1} - {num2} = {resultado}')

def multiplicacao(num1, num2):
    resultado = num1 * num2
    print(f'\nMultiplicação: \n{num1} * {num2} = {resultado}')

def divisão(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        print('\nNão é possível dividir por zero')
    else: 
        print(f'\nDivisão: \n{num1} / {num2} = {resultado}')

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
soma(num1, num2)
subtracao(num1, num2)
multiplicacao(num1, num2)
divisão(num1, num2)


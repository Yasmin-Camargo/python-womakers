''' 
1. Faça um Programa que peça dois números e imprima o maior deles
'''

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'\nO maior número é {num1}')
elif num2 > num1:
    print(f'\nO maior número é {num2}')
else:
    print('\nOs números são iguais')
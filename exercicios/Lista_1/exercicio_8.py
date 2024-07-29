'''
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês
'''

def salario(horas, valor_hora):
    salario = horas * valor_hora
    print(f'\nSalário: R$ {salario:.2f}')

horas = float(input('Digite o número de horas trabalhadas no mês: '))
valor_hora = float(input('Digite o valor da hora de trabalho: '))

if horas < 0 or valor_hora < 0:
    print('Valor inválido')
else:
    salario(horas, valor_hora)
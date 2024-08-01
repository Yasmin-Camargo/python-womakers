''' 
3. Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função
'''

def celsius_para_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperatura = float(input('Digite uma temperatura: '))
unidade = input('Digite a unidade da temperatura: \n1-Celsius \n2-Fahrenheit: ')
if unidade == '1':
    print(f'\nA temperatura em Fahrenheit é: {celsius_para_fahrenheit(float(temperatura)):.2f}')
elif unidade == '2':
    print(f'\nA temperatura em Celsius é: {fahrenheit_para_celsius(float(temperatura)):.2f}')
else:
    print('\nDigite um valor válido')
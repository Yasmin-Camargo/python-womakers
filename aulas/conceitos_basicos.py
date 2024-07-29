'''
Mensagem inicial 
para o 
usuário
'''

print('Olá Mundo!') # Este é um comentário curto
print('Este é o primeiro programa em Python no curso de Python')


# Variáveis
# Tipo inteiro = int
numero = int(input('Digite seu número: '))
print(f'O número digitado é: {numero}')

# Tipo float = float
numero = float(input('\nDigite seu número decimal: '))
print(f'O número decimal digitado é: {numero}')

# Tipo texto = string
frase = input('\nDigite sua frase: ')
print(f'A frase digitada é: {frase}')


# Operações matemáticas
# Soma = +
numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
soma = numero1 + numero2
print(f'A soma dos números é: {soma}')

# Subtração = -
numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
subtracao = numero1 - numero2
print(f'A subtração dos números é: {subtracao}')

# Multiplicação = *
numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
multiplicacao = numero1 * numero2
print(f'A multiplicação dos números é: {multiplicacao}')

# Divisão = /
numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
divisao = numero1 / numero2
print(f'A divisão dos números é: {divisao}')

# Divisão inteira = //
numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
divisao_inteira = numero1 // numero2
print(f'A divisão inteira dos números é: {divisao_inteira}')


# Incremento = +=
valor = 5
valor += 1
print(f'\nIncremento: {valor}')

# Decremento = -=
valor = 5
valor -= 1
print(f'\nDecremento: {valor}')

# Resto da divisão = %
numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
resto = numero1 % numero2
print(f'O resto da divisão dos números é: {resto}')

# Ordem de precedência = ()
calculo = (5 + 3) * ((2 + 4) * 2)
print(f'\nResultado: {calculo}')


# Operadores relacionais
# == : Igual a 
# >  : Maior que
# >= : Maior ou igual a
# <  : Menor que
# <= : Menor ou igual a
# != : Diferente de


# f-strings
valor = 45.3458372
print(f'{valor:.2f}')
nome = 'Caroline'
print(f'Olá {nome}')

# str.format()
print('Olá {}, você tem {} anos'.format('Yasmin', 22))

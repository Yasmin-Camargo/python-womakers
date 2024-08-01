'''
Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos 
'''

def soma(a, b, c):
    return a + b + c

a, b, c = input('Digite três números separados por espaço: ').split()
a, b, c = int(a), int(b), int(c)

print(f'A soma dos números é: {soma(a, b, c)}')
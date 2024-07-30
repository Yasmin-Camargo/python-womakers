'''
Faça um programa que lê três números inteiros e os mostra em ordem
crescente.
'''

list_numeros = input('Digite três números inteiros separados por espaço: ').split()
list_numeros.sort()

print('Números em ordem crescente: ')
for numeros in list_numeros:
    print(numeros)

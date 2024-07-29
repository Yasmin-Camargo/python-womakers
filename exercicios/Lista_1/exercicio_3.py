'''
Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.
'''

kilometros = float(input('Digite a quantidade de quilômetros: '))

metros = kilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10

print(f'\n{kilometros} km equivale a: ')
print(f'- Metros = {metros} m \n- Centimetros = {centimetros} cm \n- Milimetros = {milimetros} mm')
'''
Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l
'''

litros = float(input('Digite a quantidade de litros de combustível consumidos: '))
distancia = float(input('Digite a distância percorrida: '))

consumo_medio = distancia / litros

print(f'\nO consumo médio é de {consumo_medio:.2f} km/l')
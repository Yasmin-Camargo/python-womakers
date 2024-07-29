'''
6. Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
'''

def tempo_viagem(distancia, velocidade):
    tempo = distancia / velocidade
    return tempo

distancia = float(input('Digite a distância da viagem: '))
if distancia < 0:
    print('Distância inválida')
else:
    tempo_aviao = tempo_viagem(distancia, 600)
    tempo_carro = tempo_viagem(distancia, 100)
    tempo_onibus = tempo_viagem(distancia, 80)

    print(f'\nTempo de viagem: \navião: {tempo_aviao:.2f} horas')
    print(f'carro: {tempo_carro:.2f} horas')
    print(f'ônibus: {tempo_onibus:.2f} horas')
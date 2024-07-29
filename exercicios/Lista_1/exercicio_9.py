'''
Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício
'''

def total_calorias_queimadas(horas):
    calorias_por_minuto = 5
    horas_mes = 60 * 4  # 60 min por hora, 4 semanas por mês
    calorias = horas * horas_mes * calorias_por_minuto
    print(f'\nTotal de calorias queimadas no mês: {calorias} cal')

horas = float(input('Digite o número de horas de exercício físico por semana: '))
if horas < 0:
    print('Valor inválido')
else:
    total_calorias_queimadas(horas)
'''
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
'''

peso = float(input('Digite o peso (kg): '))
altura = float(input('Digite a altura (m): '))

if peso<=0 or altura<=0:
    print('Valores inválidos')
else:
    imc = peso / (altura * altura)
    print(f'\nO IMC é de {imc:.2f}')

    print('Classificação:')
    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 25:
        print('Peso normal')
    elif 25 <= imc < 30:
        print('Sobrepeso')
    else:
        print('Obesidade')

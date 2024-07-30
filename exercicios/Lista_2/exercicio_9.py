''' 
O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.
'''

pares = 0
impares = 0
num = -1

while num != 0:
    num = int(input('Digite um número: '))
    if num < 0:
        print('Apenas números positivos são permitidos')
        continue
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'\nQuantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {impares}')
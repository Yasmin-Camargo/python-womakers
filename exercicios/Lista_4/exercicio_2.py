''' 
Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721
'''

def reverso_numero(numero):
    return int(str(numero)[::-1])

try:
    numero = int(input('Digite um número inteiro: '))
except ValueError as e:
    print(f'\nErro: O tipo do dado informado esta incorreto.')  
else:
    print(f'O reverso do número {numero} é: {reverso_numero(numero)}')
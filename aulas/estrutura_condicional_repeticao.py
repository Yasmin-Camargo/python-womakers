# Estrutura condicional
numero = int(input('Digite um número: '))
if numero > 0:
    print('O numero e positivo')
else:
    print('O numero e negativo')


# Estrutura de repetição
numero = -1
while numero < 0:   # enquanto
    numero = int(input('Digite um número: '))
print("Numero positivo inserido com sucesso")

frutas = ['maça', 'banana', 'uva'] # declarando uma lista
for fruta in frutas: # para cada
    print(fruta)

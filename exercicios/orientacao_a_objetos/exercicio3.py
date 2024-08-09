## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?


def calcular_media(valores):
    tamanho = len(valores) # tamanho da lista estava sendo definido como 1
    soma = 0.0
    for valor in valores: # i não estava sendo usado, portanto não era necessário o uso do enumerate 
        soma += valor
    media = soma / tamanho
    return media # a função não estava retornando a média

continuar = True
valores = []   
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False # False estava escrito errado
    else:
        valores.append(float(valor)) # os valores não estavam sendo adicionados a lista

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))
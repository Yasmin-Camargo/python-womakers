'''
6. Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício 
'''

import random
import colorama

def sort_palavras():
    palavras = open('palavras.txt', 'r')
    lista_palavras = palavras.readlines()
    return random.choice(lista_palavras).upper()


tentativas = 6
num_letras_corretas = 0
palavra = sort_palavras()
palavra = palavra.strip()
letras_erradas = []
forca = ['_'] * len(palavra)

while tentativas > 0:
    print('\n\n\n\n === JOGO DA FORCA === \n')
    print(f'Dica: Tecnologia - A palavra tem {len(palavra)} letras')
    print(f'Numero de tentativas: {tentativas} / 6 ')
    print(f'Letras erradas: {letras_erradas}\n')
    for letra in forca:
        print(colorama.Fore.BLUE + f'{letra}', end=' ')
    print(colorama.Style.RESET_ALL)

    letra = input('\n\nDigite uma letra: ').upper()
    if letra in palavra and letra not in forca:
        print('Acertou!')
        for i in range(len(palavra)):
            if letra == palavra[i]:
                forca[i] = letra
                num_letras_corretas += 1
    elif letra not in forca and letra not in letras_erradas:
        print('Errou!')
        tentativas -= 1
        letras_erradas.append(letra)
    else:
        print('Você já tentou essa letra!')

    if num_letras_corretas == len(palavra):
        print(colorama.Fore.GREEN+'\n\nVocê acertou! :)')
        print(colorama.Style.RESET_ALL)
        print(f' --> Palavra: {palavra}')
        break

    if tentativas == 0:
        print(colorama.Fore.RED+'\n\n Você perdeu! :(')
        print(colorama.Style.RESET_ALL)
        print(f' --> A palavra era: {palavra}')

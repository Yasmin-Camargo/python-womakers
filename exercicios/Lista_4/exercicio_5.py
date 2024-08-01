'''
Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais
'''

def contar_vogais(string):
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in string:
        if letra in vogais:
            vogais[letra] += 1

    for vogal in vogais:
        print(f'{vogal.upper()}: {vogais[vogal]}')

    print(f"total de vogais {sum(vogais.values())}")

string = input('Digite uma frase: ')
contar_vogais(string)
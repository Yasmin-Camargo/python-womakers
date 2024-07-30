''' 
Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente""
'''

perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
respostas_suspeita = 0

for pergunta in perguntas:
    resposta = input(pergunta + ' (s/n): ').upper()
    if resposta == 'S':
        respostas_suspeita += 1
    elif resposta != 'N':
        while resposta != 'S' and resposta != 'N':
            print('Resposta inválida, digite "s" para sim ou "n" para não')
            resposta = input(pergunta + ' (s/n): ').upper()
            if resposta == 'S' or resposta == 'N':
                respostas_suspeita += 1
                break

if respostas_suspeita == 2:
    print('\nVocê é considerado suspeito')
elif respostas_suspeita == 3 or respostas_suspeita == 4:
    print('\nVocê é considerado cúmplice')
elif respostas_suspeita == 5:
    print('\nVocê é considerado assassino')

    
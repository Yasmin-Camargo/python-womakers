'''
Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0. 
'''

alunos = []
aprovados = 0

for i in range(5):
    notas = []

    for j in range(4):
        nota = float(input(f'Insira a {j+1}ª nota do {i+1}º aluno: '))
        if nota < 0 or nota > 10:
            while nota < 0 or nota > 10:
                print('Nota inválida, digite um valor entre 0 e 10')
                nota = float(input(f'-> Nova nota: '))
        notas.append(nota)

    media = sum(notas) / 4
    alunos.append(media)

    if media >= 7:
        aprovados += 1

    print("\n")

print(f'\nMédias dos alunos: {alunos}')
print(f'\n{aprovados} alunos tiveram média maior ou igual a 7.0')


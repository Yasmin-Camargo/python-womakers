'''
Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome
'''

contatos = {}

while True:
    nome = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone do contato: ')
    contatos[nome] = telefone

    continuar = input('\nDeseja adicionar mais contatos? (s/n): ').upper()
    if continuar == 'N':
        break

while True:
    busca = input("\nDigite o nome do contato que deseja procurar: ")
    if busca in contatos:
        print(f'\n{busca}: {contatos[busca]}')
    else:
        print('\nContato não encontrado')

    continuar = input('\nDeseja procurar mais contatos? (s/n): ').upper()
    if continuar == 'N':
        break

print("\nContatos: ")
for nome, telefone in contatos.items():
    print(f'- {nome}: {telefone}')
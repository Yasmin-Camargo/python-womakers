'''
Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra
'''

carrinho = {}
total = 0

while True:
    produto = input('Digite o nome do produto: ')
    quantidade = int(input('Digite a quantidade do produto: '))

    carrinho[produto] = quantidade

    continuar = input('\nDeseja adicionar mais produtos ao carrinho? (s/n): ').upper()
    if continuar == 'N':
        break

print("\nProdutos: ")
for produto, quantidade in carrinho.items():
    print(f'- {quantidade} {produto}')

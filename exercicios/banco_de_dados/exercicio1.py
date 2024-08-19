'''
1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
3. Consultas Básicas
    a) Escreva consultas SQL para realizar as seguintes tarefas:
        i) Selecionar todos os registros da tabela "alunos".
        ii) Selecionar o nome e a idade dos alunos com mais de 20 anos.
        iii) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
        iv) Contar o número total de alunos na tabela.
4. Atualização e Remoção
    a) Atualize a idade de um aluno específico na tabela.
    b) Remova um aluno pelo seu ID.
5. Criar uma Tabela e Inserir Dados
    a) Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).
    b) Insira alguns registros de clientes na tabela.
6. Consultas e Funções Agregadas
    a) Escreva consultas SQL para realizar as seguintes tarefas:
        i) Selecionar o nome e a idade dos clientes com idade superior a 30 anos.
        ii) Calcular o saldo médio dos clientes.
        iii) Encontrar o cliente com o saldo máximo.
        iv) Contar quantos clientes têm saldo acima de 1000.
7. Atualização e Remoção com Condições
    a) Atualize o saldo de um cliente específico.
    b) Remova um cliente pelo seu ID.
8. Junção de Tabelas
    a) Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real).
    b) Insira algumas compras associadas a clientes existentes na tabela "clientes".
    c) Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
'''

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# EXERCÍCIO 1
print('\n ---> EXERCÍCIO 1')
print('Criando tabela alunos')
'''
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')
'''

# EXERCÍCIO 2
print('\n ---> EXERCÍCIO 2')
print('Inserindo dados')
'''
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Yasmin", 22, "Ciência da Computação");')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Caroline", 22, "Ciência da Computação");')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Elizabeth", 58, "Contabilidade");')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "João", 25, "História");')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Maria", 33, "Letras");')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "ana", 18, "Engenharia");')
'''


# EXERCÍCIO 3
print('\n ---> EXERCÍCIO 3')
print('Consultas')
consulta = cursor.execute('SELECT * FROM alunos;')
consulta = cursor.execute('SELECT nome,idade FROM alunos WHERE idade > 20;')
consulta = cursor.execute('SELECT nome FROM alunos WHERE curso == "Engenharia" ORDER BY nome;')
consulta = cursor.execute('SELECT COUNT(*) FROM alunos;')

for dados in consulta:
    print(dados)

# EXERCÍCIO 4
print('\n ---> EXERCÍCIO 4')
print('Deletando e atualizando dados')
'''
cursor.execute('UPDATE alunos SET idade = 16 WHERE nome = "ana";')
cursor.execute('DELETE FROM alunos WHERE id = 5;')
'''

# EXERCÍCIO 5
print('\n ---> EXERCÍCIO 5')
print('Criando tabela clientes e inserindo dados')
'''
cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo REAL);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Yasmin", 22, 5000.00);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Caroline", 22, 2000.00);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Elizabeth", 58, 2000.00);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "João", 25, 4000.00);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Maria", 33, 5000.00);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(6, "ana", 18, 1000.00);')
'''

# EXERCÍCIO 6
print('\n ---> EXERCÍCIO 6')
print('Consultas')

consulta = cursor.execute('SELECT nome,idade FROM clientes WHERE idade > 30;')
consulta = cursor.execute('SELECT AVG(saldo) FROM clientes;')
consulta = cursor.execute('SELECT nome FROM clientes WHERE saldo == (SELECT MAX(saldo) FROM clientes);')
consulta = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000;')

for dados in consulta:
    print(dados)

# EXERCÍCIO 7
print('\n ---> EXERCÍCIO 7')
print('Atualizando e deletando dados')
'''
cursor.execute('UPDATE clientes SET saldo = 8000.00 WHERE nome = "Yasmin";')
cursor.execute('DELETE FROM clientes WHERE id = 5;')
'''

# EXERCÍCIO 8
print('\n ---> EXERCÍCIO 8')
print('Criando tabela compras, inserindo dados e fazendo consulta')
'''
cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 2, "Celular", 1100.00);')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "Notebook", 1200.00);')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 1, "Curso de Ingles", 7000.00);')
'''

consulta = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id;')
for dados in consulta:
    print(dados)

conexao.commit() 
conexao.close() 
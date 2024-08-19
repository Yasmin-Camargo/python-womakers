import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT;')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone;')

#cursor.execute('DROP TABLE produtos;')

#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(1, "Yasmin", "Pelotas", "yasmin@gmail.com", 5199999999)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(2, "Maria", "Salvador", "maria@gmail.com", 5199444)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(3, "Jose", "Curitiba", "jose@gmail.com", 51923874999)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES(4, "Marcia", "Sao Paulo", "marcia@gmail.com", 5199990932)')

#cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(4, "Marcia", "Sao Paulo", "marcia@gmail.com")')
#cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(1, "João", "São Paulo", "joao@gmail.com")')
#cursor.execute('INSERT INTO gerentes(id, nome, endereco, email) VALUES(8, "Cyntjia", "Inglaterra", "cyin@gmail.com")')

#cursor.execute('DELETE FROM usuario WHERE id = 1;')
#cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome = "Jose";')

# ORDER BY e DESC
# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome,id DESC;')

# LIMIT e DISTINCT
# dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 2;')

# GROUP BY e HAVING
# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3;')


# JOIN's
# JOIN - INNER JOIN = retorna apenas os registros que possuem correspondência nas duas tabelas
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id;')

# JOIN - LEFT JOIN = retorna todos os registros da tabela à esquerda e os registros correspondentes da tabela à direita
# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id;')

# JOIN - RIGHT JOIN = retorna todos os registros da tabela à direita e os registros correspondentes da tabela à esquerda
# dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.id = gerentes.id;')

# JOIN - FULL JOIN = retorna todos os registros da tabela à direita e à esquerda
# dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.id = gerentes.id;')

# SUB-CONSULTAS
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes);')

for usuario in dados:
    print(usuario)


conexao.commit() # As informações só vão para o banco de dados quando o commit é chamado
conexao.close() # garante que processo é encerrado
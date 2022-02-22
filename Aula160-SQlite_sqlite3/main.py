"""
SQLite Base de Dados.
"""

import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # <- id aqui vai gerar auto, 1,2,3... pq é auto incremento.
#                'nome TEXT,'  # <- campo nome(key) vai receber valor do tipo 'str' que é TEXT em SQL.
#                'peso REAL'  # <- campo peso (key) vai receber valor do tipo 'float' que é REAL em SQL
#                ')')  # OBS: INTEGER = 'int'
#
# # Comando INSERT é para inserir dos dados, e VALUES é o campo do que vai ser recebido. Se tiver STR tem que ser entre ""
# # o ?, ? diz que vai receber o valor estando em uma TUPLA (), já que é mais seguro e evita preenchimento auto.
# # a cada execução do arquivo, conforme estava antes: ("Luiz Otavio", 80.5)
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Luiz Otavio", 80.5)')
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
#
# # Gerando com um dicionário:
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',  # <- Indicando qual key(:) vai receber valor
#                {'nome': 'Joãozinho', 'peso': 25}  # <- 'key' (chave) recebendo o valor.
#                )
# # Outra forma:
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'Daniel', 'peso': 113}  # Como estou manddo NONE o 'Autoincrement' lá fará o job.
#                )
#
# conexao.commit()  # <-- Comando para Inserir os dados no banco de dados.

# Alterando um dado:
# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id', {'nome': 'Joana', 'id': 2})
# conexao.commit()

# Deletando um dado:
# cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 2})  # Apaga da tabela onde estiver o ID 2

# cursor.execute('SELECT * FROM clientes')  # Comando para executar tudo (*) o que tiver em (FROM) clientes.
# for linha in cursor.fetchall():  # <- Comando para "buscar" os valores e mostrar.
#     ident, nome, peso = linha  # <- Desempacotando, pq ela vem em TUPLAS a tabela criada.
#     print(ident, nome, peso)  # <- Tendo acesso a eles separadamente.

cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso', {'peso': 50})  # <- especificando o valor do 'peso'
for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)

cursor.close()
conexao.close()

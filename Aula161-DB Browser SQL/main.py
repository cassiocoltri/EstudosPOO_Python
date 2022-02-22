import sqlite3

# OBS: Os comandos em CAIXA ALTA, são do SQL, por padrão/convenção ele é desta forma.


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)  # Esse arg estará "conectando" o arquivo do SQL feito no programa SQL3
        self.cursor = self.conn.cursor()  # Esse arg esta recebendo o "link do arquivo conectado" para as execuções

    def inserir(self, nome, telefone):
        # O arg consulta esta recebendo já uma previa de valor com (?, ?) justamente para evitar a inclusão de dados
        # automaticamente. Por isso será nescessario colocar os argumentos/valores em TUPLAS ().
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'  # funcionaria com Dict {:nome...} tb.
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()  # <- Esse comando é o que executa a func. estremamente importante.

    def editar(self, nome, telefone, ident):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE ident=?'
        self.cursor.execute(consulta, (nome, telefone, ident))
        self.conn.commit()

    def excluir(self, ident):
        consulta = 'DELETE FROM agenda WHERE ident=?'
        self.cursor.execute(consulta, (ident, ))  # <- como é uma tupla, e não se tem o 2ª atributo, se coloca ", "
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')  # O '*'  representa 'tudo'

    def buscar(self, nome):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{nome}%', ))  # O %....% é parâmetro de pesquisa em qualquer lugar dos dados.

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.inserir('Cassio', '48-99840.0806')
    agenda.inserir('Luiz', '48-11111.2222')
    agenda.inserir('Luiz K.', '48-22222.3333')
    agenda.inserir('Jossé Luiz', '48-33333.4444')
    agenda.inserir('Gustavo Luiza', '48-44444.5555')
    agenda.inserir('Patricia Luis', '48-55555.6666')
    agenda.listar()
    print()
    # agenda.editar('Miguel', '11-23456.7889', 9)
    # agenda.excluir(9)
    # agenda.listar()
    agenda.buscar('Lui')  # Como tem o % ele vai varrer e pegar tudo o que tiver correspondente (LIKE) a palavra.

"""
public, protected, private -> Tipos de OO em outras linguagens como Java.

Por convenção, em Python se usa _ e __ (um e dois underline)

_ -> Protected (Pycharm nem mais vai avisar que existe esse atributo ao digitar "var." (aperece uma list de opções)
Seria um "privado fraco"

__ -> Privado: Não mexe ai carai!!

"""


class BaseDeDados:

    def __init__(self):
        self._dados = {}  # inicialmente cliando um dicionario vazio.

    def inserir_cliente(self, id, nome):  # func para incluir clientes.
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}  # caso não exista a "chave" 'clientes' ele vai criar uma.
        else:
            self._dados['clientes'].update({id: nome})  # caso já tenha, só vai atualizar a lista com Id e nome

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, "Cassio")
bd.inserir_cliente(2, "Ronconi")
bd.inserir_cliente(3, "Coltri")
bd.apaga_cliente(2)
bd.lista_clientes()

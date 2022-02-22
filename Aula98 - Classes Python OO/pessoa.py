# Funções DENTRO das classes são chamadas de "métodos", existe apenas na classe, não pode usar fora.

from datetime import datetime

class Pessoa:

    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    # Func "__init__" existe apenas do Pyhton. Aqui essa função vai iniciar já recebendo parâmetros já estabelecidos.

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome  # self. é pq ele vai receber o parâmetro que a pessoa colocar, e salvar/retornar na var.
        self.idade = idade  # Ex: Aqui a "idade" vai receber o que a pessoa colocar como idade "var.idade = x"
        self.comendo = comendo
        self.falando = falando

    # nesse "Método" (como se chama as func dentro de classes) estou acessando o atributo "comendo=False" do __inti__
    # e trocando para "True" pela função. Sem alterar a original.

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} está comendo e não pode falar!")
            return

        if self.falando:
            print(f"{self.nome} já esta falando!")
            return

        print(f"{self.nome} está falando sobre {assunto}")
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando.")
            return
        print(f"{self.nome} parou de falar!")
        self.falando = False

    def comer(self, alimento):  # Essa func foi criada apenas para pegar o "self.comendo" e colocando para True.

        if self.comendo:  # Aqui checando se a var já foi executada antes (true) ele entra aqui para ñ executar again.
            print(f"{self.nome} já está comendo!")
            return

        if self.falando:
            print(f"{self.nome} não pode comer falando.")
            return

        print(f"{self.nome} está comendo {alimento}")
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não esta comendo.")
            return

        print(f"{self.nome} parou de comer.")
        self.comendo = False

    def ano_de_nascimento(self):
        return print(f"{self.nome} nasceu em {self.ano_atual - self.idade}")

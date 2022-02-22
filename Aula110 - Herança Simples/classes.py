class Pessoa:  # Conhecida na comunidade como SUPER CLASSE (pai, mãe etc...)
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__  # <- Usando para mostrar ou especificar qual classe esta usando.

    def falar(self):  # <- Falar perten-se a todos.
        print(f"{self.nomeclasse} esta falando...")


# Para não ficar "repetitivo" a parte de nome e idade para todo mundo, a Herança serve para atribuir as mesmas
# qualificações, no caso colocando a nova classe em (parenteses) ela esta "herdando" as funções da mãe/pai.

# SUBCLASSES: (eles podem ter expecificações mesmo herdando da SuperClasse.


class Cliente(Pessoa):  # <- Seria a mesma coisa que colocar abaixo as info:
    # def __init__(self, nome, idade):
    #     self.nome = nome
    #     self.idade = idade

    def comprar(self):  # <- Comprar só vai pertencer ao Cliente
        print(f"{self.nomeclasse} esta comprando...")


class Aluno(Pessoa):

    def estudar(self):  # <- Estudar só vai percenter ao Aluno.
        print(f"{self.nomeclasse} esta estudando...")

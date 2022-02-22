"""
Diferenças entre @classmethod, @staticmethod e intancias(self)

@classmethod e @staticmethod eles retornam apenas para a Classe (class) do programa. Pois é um "decorador"
Ja o outro, precisa da instancia, no caso (self.) recebendo algum valor, ex: p1 = Pessoa(nome, idade)

Obs: o @staticmehod não precisa da Classe ou instância.

@classmethod -> Referencia a Classe

Func normal dentro da Class (def valor_da_func) -> Referencia a instancia!

@staticmethod -> Ele referencia tanto Class como isntacia, porem NÂO se pode acessar os "self" ou "cls" alheio
das demais funções, pois ele é estático.

"""

from random import randint

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod  # o @classmethod ele "decora" uma configuração de classe (cls) em convenção.
    def por_ano_nascimento(cls, nome, ano_nascimneto):
        idade = cls.ano_atual - ano_nascimneto
        return cls(nome, idade)  # Ele vai retornar o cls (Classe Pessoa)

    @staticmethod
    def gera_id():
        rand = randint(1000, 9999)  # var rand só vai funcionar AQUI, ele não pode ser acessado por fora.
        # não daria para atribuir uma var. Ex: variavel = self.nome ou cls.nome
        return rand



p1 = Pessoa.por_ano_nascimento("Luiz", 1987)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print("#" * 60)
print(Pessoa.gera_id())  # ele vai funcionar tanto só por classe
print(p1.gera_id())  # tanto por instancia, chamando alguma var atrelada. No caso aqui "p1."

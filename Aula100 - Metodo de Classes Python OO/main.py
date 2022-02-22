
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


p1 = Pessoa.por_ano_nascimento("Luiz", 1987)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

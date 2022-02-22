"""
O que são Dataclasses?
O módulo Dataclasses fornece um decorador e funções para criar automaticamente métodos como:
__init__(), __repr__(), __eq__ (etc) em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: http://docs.python.org/pt-br/3/library/dataclasses.html

Resumo: método dataclasse não precisa mais colocar o init e outros cod mais complexos, ele faz automaticamente.
"""

from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


# Por padrão, eles vem com as condições: (eq=True, repr=True, ,order=True, frozen=False, init=True)

# O que estiver dentro do () com "=False" são funções prévias que estamos DESATIVANDO.
@dataclass(eq=False)
class Pessoa:
    nome: str  # <- var: e espessificando o tipo de entrada, aqui str = string
    sobrenome: str = field(repr=False)  # <- aqui estou desativando o "repr" apenas nessa var, usando o filed()

    def __post_init__(self):  # <-- Esse post_init executa automaticamente, mesma coisa que a func DEF abaixo.
        self.nomecompleto = f"{self.nome} {self.sobrenome}"

    @property  # <-- aceita todos os tipos de métodos, setters, getters etc... OBS: Property é um Getter!
    def nomecompleto2(self):
        return f"{self.nome} {self.sobrenome}"


p1 = Pessoa("A", "5")
p2 = Pessoa("C", "3")
p3 = Pessoa("D", "4")
p4 = Pessoa("B", "6")

pessoas = [p1, p2, p3, p4]
print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))
# # Repare que o Sobrenome não vai aparecer pq no filed() foi desativado o repr para "False"

# print(p1)
# print(p1 == p2)  # <-- no dataclass já esta implicito a func __eq__ (igual) para comparar, tem como desativar.
# print(p1.nome)
# print(p1.sobrenome)
# print(p1.nomecompleto)
# print(p1.nomecompleto2)

print("*********************************")
print(asdict(p1))
print(astuple(p1))

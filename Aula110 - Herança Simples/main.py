from classes import Cliente, Aluno

"""
Associação: USA | Agregação: TEM | Composição: É dona | Herança: É um objeto tb.
"""

c1 = Cliente("Luiz", 45)
print(c1.nome)
c1.falar()
c1.comprar()

print()

a1 = Aluno("Maria", 54)
print(a1.nome)
a1.falar()
a1.estudar()

class A:
    def falar(self):
        print("Estou falando em A")


class B(A):
    def falar(self):
        print("Estou falando em B")


class C(A):
    def falar(self):
        print("Estou falando em C")


# Herança Multipla, aqui esta herdando de B e C. Python vai procurar da esq p/direita quando for procurar alguma func.
class D(B, C):
    pass

d = D()
d.falar()  # Ele vai pegar do "B", caso não localiza, vai procurar no "C", e  se  não achar, vai no "A".


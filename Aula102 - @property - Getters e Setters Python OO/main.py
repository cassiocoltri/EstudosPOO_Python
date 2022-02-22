class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcento):
        self.preco = self.preco - (self.preco * (porcento / 100))

    # Getter -> Vai pegar alguma coisa.
    @property
    def preco(self):
        return self._preco  # por convenção, se coloca uma "_" underline na frente da var na qual queres referenciar.
                            # do contrário poderia dar algum erro de loop pois ela já estaria com o mesmo nome acima.

    # Setter -> Vai "setar" o que foi "pego" pelo getter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ""))
        self._preco = valor

    @property
    def nome(self):  # pegando a var nome
        return self._nome

    @nome.setter
    def nome(self, valor):  # tratando a var nome.
        self._nome = valor.title()  # <- essa func torna só a primeira letra Maiuscula.


p1 = Produto("CAMISA", 50)  # <- Nota-se que foi colocado em maiusculo porem vai ser "setado" minúsculo.
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto("CANECA", "R$15")
p2.desconto(10)
print(p2.nome, p2.preco)

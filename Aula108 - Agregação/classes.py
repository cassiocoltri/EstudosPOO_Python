"""
Agragação de classes, uma precisa da outra para funcionar.

Ex: Carro e Rodas. Eles existem separadamente, porem um carro não pode funcionar sem as rodas.
E as rodas não podem andar sem um caro junto.
"""


class CarrihnoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

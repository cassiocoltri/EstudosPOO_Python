"""
Interador.
Aula mais para mostrar o que ocorre debaixo dos panos, pq uma lista [] já tem todos esse métodos.
"""


class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, valor):
        if index >= len(self.__items):
            self.__items.append(valor)
        self.__items[index] = valor

    def __delitem__(self, index):
        del self.__items[index]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item

        except IndexError:  # <-- Quando acabar as "voltas" no for, da interação, vai dar o erro: "IndexError"
            raise StopIteration  # <-- quando isso acontecer, ele vai detectar pelo "except" e "levantar"/raise
        # o comando para parar as interações, o "StopIteration".

    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('Luiz')
    lista.add('Otavio')
    lista.add('Miranda')
    lista[3] = "Jumento"

    del lista[2]

    print(lista)
    # for valor in lista:
    #     print(valor)

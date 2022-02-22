class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None  # <-- Privado!

    @property
    def nome(self):  # pegando daqui <- que está "retornando" ao self.__nome do init setado inicialmente.
        return self.__nome

    @property
    def ferramenta(self):  # Definindo o "privado" como atributo.
        return self.__ferramenta

    @ferramenta.setter  # Setando, especificando que o "atributi" sera setado com algum valor.
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta  # <- Setando o que for lançado de argumento.


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print("Caneta esta escrevendo...")


class MaquinaDeEscrever:
    def escrever(self):
        print("Maquina esta escrevendo...")

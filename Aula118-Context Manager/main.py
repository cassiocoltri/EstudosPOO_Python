"""
Gerenciador de Contextos.
"""


# Forma 01 de criar o gerenciador de contextos.

class Arquivo:

    def __init__(self, arquivo, modo):
        print("abrindo arquivo")
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print("retornando arquivo")
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("fechando arquivo")
        self.arquivo.close()
        # Tratei arquivo de exeção.
        return True


with Arquivo("abc.txt", "w") as arquivo:
    arquivo.write("Alguma Coisa")

# Forma 02 de criar (Sem precisar criar uma classe):
print("########## Forma 2 ############")

from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(arquivo, modo)
        yield arquivo  # <-- Usando isso (yield) pq tem o "decorador" @contextmanager
    finally:
        print("Fechando arquivo")
        arquivo.close()


with abrir("abc2.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")

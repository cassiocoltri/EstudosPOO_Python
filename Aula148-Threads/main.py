from time import sleep
from threading import Thread
from threading import Lock  # <- "Tranca", como se fosse uma porta com fechadura.

"""
class MeuThread(Thread):
    # Lembrando que no Init, ele esta passando já previamente TODOS os args/kwars nescessários para as aplicações.
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):  # <- por isso, aqui só precisa do SELF, já que os outros args (texto e tempo) já estão no INIT.
        sleep(self.tempo)
        print(self.texto)


# Os Threads executam paralelamente junto com o "main cod", ele não esperaria "chegar na vez dele" para executar.

t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 7)
t3.start()


for i in range(10):
    print(i)
    sleep(1)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


# O "target=" estou mandando ele apontar para a funcão "vai_demorar", o "args=" é pq ela(func) precisa de argumentos.

t1 = Thread(target=vai_demorar, args=('Ola Munto', 4))
t1.start()

t2 = Thread(target=vai_demorar, args=('Ola Planeta', 6))
t2.start()

t3 = Thread(target=vai_demorar, args=('Ola Universo', 8))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Ola Munto', 10))
t1.start()
t1.join()

print('Thread acabou!')
"""


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()  # <-- ativando a func Lock. Ela é como uma "tranca" e deixa sempre uma execução por vez.

    def comprar(self, qtd):
        self.lock.acquire()  # <- Primeiro que entrou passou a "chave", para terminar o codigo.

        if self.estoque < qtd:
            print("Não temos lugares suficiente.")
            self.lock.release()
            return
        sleep(1)
        self.estoque -= qtd
        print(f"Voce comprou {qtd} ingresso(s).\nAinda temos {self.estoque} em estoque.")
        # print()
        self.lock.release()  # <- Liberando para o outro Thread.


if __name__ == '__main__':
    ingressos = Ingressos(10)

    threads = []

    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    executando = True
    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingressos.estoque)

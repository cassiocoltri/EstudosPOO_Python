"""
Pilhas e Filas.
Pilhas (stack) LIFO -> last in, first out.
    Ex: Pilha de livros que são adicionados um sobre o outro.

Fila (queue) - FIFO -> fist in, first out.
    Ex: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos coletarais em desempenho, porque a cada item alterado, todos os índices serão modificados.
"""

from collections import deque
from time import sleep

fila = deque()
fila.append('Joãozinho')
fila.append('Maria')
fila.append('Otavio')
fila.append('Marcos')
fila.append('José')
fila.popleft()  # <- função tira o primeiro item da lista. É o verso do .pop()
print(fila)

for nome in fila:
    print(nome)

print('####' * 30)
fila2 = deque(maxlen=5)  # <- aqui estamos delimitando a qdt maxima de itens que pode ter.
fila2.extend([1, 2, 3, 4])
fila2.append(5)
fila2.append(6)
fila2.append(7)  # <- O ultimo adicionado vai sempre retirar o "primeiro" e fazendo a "fila andar"
print(fila2)

print('####' * 30)
fila3 = deque(maxlen=10)

for i in range(100):
    fila3.append(i)
    sleep(.05)
    print(fila3)
"""
Algumas funçõesdo deque():
    var.appendleft() -> Acrescenta itens a Esquerda (contrario do append normal)
    var.reverse() -> Reverte toda a fila. [1,2,3] vira [3,2,1]
    var.extendleft() -> Acrescenta itens a partir da Esquerda, é o inverso do extend()
    var.rotate() -> Rotaciona o elemento, ex: [A,B,C,D,E] rotate(2) vai inverter os dois últimos: [D,E,A,B,C]
    var.count() -> "Conta" a quantidade de elementos: Ex: [A,A,A,B,C] count(A) vai retornar "3".
"""

teste = deque()
teste.extend(['a', 'a', 'a', 'a', 'a', 'a', 'b', 'c', 'd'])
print(teste.count('a'))

"""
http://docs.python.org/3.0/library/datetime.html
As diretrizes estão no link, %alguma coisa faz algo. %d = dia %m = mês etc...
"""
from datetime import datetime, timedelta
from locale import setlocale, LC_ALL  # <-- Aqui para deixar localizado para pt-br

setlocale(LC_ALL, 'pt_BR.utf-8')  # <-- o '' vazio ele pega o local do computador, nocaso aqui pt-Br
# já colocando o 'pt_BR.utf-8' ele esta excludivamente pegando em pt-br, mesmo se eu estivesse em outro pais.

dt = datetime.now()
formatacao = dt.strftime('%A, %d de %B de %Y')
print(formatacao)

# index:        ano  mes dia hr  min seg
data = datetime(2019, 4, 20, 10, 53, 20)
data = data + timedelta(days=5, seconds=59)  # Func timedelta soma/acrescenta tempo na data, dia, minutos, segundos etc

# Func datetime.strptime recebe dados em STR (primeiro arg) e faz a converção (segundo arg)
data2 = datetime.strptime('20/04/2019', '%d/%m/%Y')

print(data.strftime('%d/%m/%Y'))
print(data2)

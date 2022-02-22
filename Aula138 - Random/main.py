"""
Func(Módulo) Random´s
"""

import random
import string

# Gera um Número inteiro entre A e B
inteiro = random.randint(10, 20)

# Gera um número aleatório usando a função range()
inteiro2 = random.randrange(900, 1000, 10)

# Gera um Número flutuante(real com ,) entre A e B
flutuante = random.uniform(10, 20)

# Gera um número Flutuante entre 0 e 1:
flutuante2 = random.random()

print(f"{inteiro} numero gerado INT entre A[10] e B[20]")
print(f"{inteiro2} numero gerado INT entre RANGE de 900 a 1000 pulando entre 10 em 10")
print(f"{flutuante:.2f} numero gerado FLOAT entre A[10] e B[20]")
print(f"{flutuante2} numero gerado FLOAT entre 0 e 1")
print()
print("##" * 50)
print()

lista = ['Luiz', 'Otavio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
sorteio = random.choices(lista)  # <- Função retorna elementos de 1 a x.
sorteio2 = random.choices(lista, k=2)  # <- Função "k=x" vai retornar "x" resultado. no ex são 2 (pode dar repetido).
sorteio3 = random.sample(lista, 2)  # <- Essa função retorna "x" elemantos, porem não repeditos.
sorteio4 = random.choice(lista)  # Func choise retorna apenas UM elemento.

print(sorteio)
print(sorteio2)
print(sorteio3)
print(sorteio4)

random.shuffle(lista)  # <-- Essa função "embaralha" os dados de uma lista.
print(lista)

# Gerando uma lista Aleatória:
letras = string.ascii_letters  # <- Retorna letras 'Maiusc (A-Z)' e 'minusc (a-z)'
# variável = string.ascii_lowercase: Retorna letras "minusculas" apenas
# variável = string.ascii_uppercase: Retorna letras "Maiusculas" apenas.
digitos = string.digits  # <- retorna digitos (0 a 9).
caracteres = '!@#$%¨&'

geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))  # Criando uma lista str vazia ("") e unindo todos as STR

print(letras)
print(digitos)
print(senha)

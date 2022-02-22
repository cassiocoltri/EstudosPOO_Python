"""
JavaScript Object Notation - JSON
JSON é um formato de troca de dados entre sistemas e programas muito leve e fácil utilização.
Muito utilizado em APIs
"""

from dados import *
import json

# dados_json = json.dumps(clientes_dicionarios, indent=4)  # "indent=4" para deixar melhor (espaçamento), mais "visivel"
# print(dados_json)
#
# dicionario = json.loads(clientes_json)
#
# for chave, valor in dicionario.items():
#     print(chave)
#     print(valor)

# Convertendo arquivo em JSON:
with open('clientes.json', 'w') as arquivo:  # Formado 'w' é de formado para escrita.
    json.dump(clientes_dicionarios, arquivo, indent=4)

# Abrindo o arquivo JSON:
with open('clientes.json', 'r') as arquivo:  # <-- "r" de row, lendo a linha.
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave)
    print(valor)

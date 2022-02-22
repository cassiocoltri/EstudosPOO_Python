"""
Comma Separated Values ou CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), base de dados, clientes de e-mail etc...
"""

import csv  # <-- Para ler arquivos .CSV deve-se importar esse metódo.

with open('clientes.csv', 'r') as arquivo:
    # dados = csv.reader(arquivo)
    # dados = csv.DictReader(arquivo)  # <- Aqui para retornar com um Dicionário {'chave': 'valor'}.
    dados2 = [x for x in csv.DictReader(arquivo)]  # <-- Usando listcomp para salvar/converter em uma Lista.

    # for dado in dados:
    #     print(dado['Nome'], dado['Sobrenome'])


# OBS: o que esta entre ['var'] equivale ao conteúdo(coluna Excel como exemplo),
# no caso acima vai pegar o que tem chave/valor "Nome", "Sobrenome" e retornar.

for dado in dados2:  # <- Não daria para fazer isso em "dados" pq ele esta fora do arquivo with e como ele é um
    # interador, ele "gastou" os dados em cada 'next' apresentado. Já o "dados2" como é uma lista dá de boas.
    print(dado)

# Escrevendo um novo arquivo:
with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo, delimiter=',',  # <-- Delimitando o arquivo para ser separado por "," virgula.
        quotechar='"',  # <-- Esse comando coloca os char em "" (aspas duplas).
        quoting=csv.QUOTE_ALL  # <-- aqui para aplicar em TUDO o comando acima.
    )

    chaves = dados2[0].keys()  # <-- Aqui estou pegando as "keys" os valores que tem dentro da lista, os "nomes"
    chaves = list(chaves)  # convertendo em Lista
    escreve.writerow(  # escrevendo da lista[0] a lista ultima (no caso foi 3)
        [
            chaves[0],  # Nome
            chaves[1],  # Sobrenome
            chaves[2],  # E-mail
            chaves[3]  # Telefone
        ]
    )

    for dado in dados2:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )

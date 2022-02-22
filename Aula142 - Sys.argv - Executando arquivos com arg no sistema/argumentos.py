import sys
import os

# print('Olar Mundao!')

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print("Faltando argumentos:")
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')  # <-- sep= só para deixar um "tab" no print.
    print('-d', 'Para listar todos os diretorios nesta pasta', sep='\t')
    sys.exit()

so_arquivos = False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):  # <-- o "." esta definindo essa pasta como o caminho, mas poderia colocar qualquer um.
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)
    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)

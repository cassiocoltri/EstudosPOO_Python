"""
shutil -> Move e executa arquivos.
"""
import os
import shutil

caminho_original = f'C:/Users/carla/Downloads/Procuração'
caminho_novo = f'C:/Users/carla/Downloads/serie2'

try:
    os.mkdir(caminho_novo)  # <-- Esse os.mkdir comando para cria a pasta.
except FileExistsError as e:
    print(f"Pasta {caminho_novo} já existe.")

# DICA: Normalmante as VAR/ARG em "plural" esta relacionado a mais de uma coisa, já os Singulares em pegar X coisa.

# P  raiz, pastas, arqvos em caminho x...
for root, dirs, files in os.walk(caminho_original):
    for file in files:  # <- Arquivo em Arquivos
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.jpg' in file:  # <- Aqui estou colocando para copiar só o que contem '.jpg' no nome.
            # shutil.move(old_file_path, new_file_path)  # <-- Esse comando MOVE, como se fosse um Ctrl+x Ctrl+v
            # print(f"Arquivo {file} movido com sucesso!")
            shutil.copy(old_file_path, new_file_path)  # <-- Esse comando COPIA, como se fosse um Ctrl+c Ctrl+v
            print(f"Arquivo {file} copiado com sucesso!")

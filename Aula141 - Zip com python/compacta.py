from zipfile import ZipFile
import os

caminho = r'C:\Users\carla\Downloads\serie2'  # <-- caminho padrão.

# ANEXANDO ARQUIVOS NO ZIP:

with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):  # <-- List DIR, listando os "diretórios" quais arquivos tem nesse caminho.
        caminho_completo = os.path.join(caminho, arquivo)  # o os.path.join() serviu para atrelar o "caminho" + arquivo
        # C:\Users\carla\Downloads\serie2\nome_dos_arquivos
        zip.write(caminho_completo, arquivo)  # <- Segundo ARG do zip.write ele deixa o "nome" do arquivo apenas.
        # do contrário, ficaria o "endereço (C:\Users\carla\Downloads\serie2\nome_dos_arquivos)"

# LENDO ARQUIVO ZIP:

with ZipFile('arquivo.zip') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# DESCOMPACTANDO/EXTRAINDO ARQUIVOS ZIP:

with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('nome_da_pasta')  # <-- func para jogar tudo e dentro do () vai o "nome da pasta"

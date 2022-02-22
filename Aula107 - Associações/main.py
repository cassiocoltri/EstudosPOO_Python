from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor("Joãozinho")
print(escritor.nome)  # repare que o ".nome" ele esta pegando do @property da classe Escritor.
caneta = Caneta("Bic")
maquina = MaquinaDeEscrever()

# Estou pegando o escritor (Classe) e puxando a variável privada para receber o atributo que esta na classe Maquina

escritor.ferramenta = maquina  # <-- Chama-se associação. Método mais "fraco" em questão de segurança.

escritor.ferramenta.escrever()  # chamando tudo no método (func) e eecutando.

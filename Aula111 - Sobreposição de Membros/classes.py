class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__  # <- Usando para mostrar ou especificar qual classe esta usando.

    def falar(self):  # <- Falar perten-se a todos.
        print(f"{self.nomeclasse} esta falando...")


class Cliente(Pessoa):

    def comprar(self):
        print(f"{self.nomeclasse} esta comprando...")

    def falar(self):
        print("Estou em CLIENTE")


class ClienteVip(Cliente):  # <- Aqui ele esta recebendo/herdando o que tem no "Cliente" e implícitamente no "Pessoa"

    def __init__(self, nome, idade, sobrenome):  # <- Usando uma func __intit__, porem aqui esou usando o "super()"
        super().__init__(nome, idade)  # <-- Ele vai executar o que tiver superior com o mesmo nome da classe.
        # Pessoa.__init__ -> funcionaria TB, no lugar do super(), pois ele esta pegando DIRETAMENTE da "class Pessoa"
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)  # <- Aqui executando SEM precisar do super(), tenho que instanciar de onde vem
        Cliente.falar(self)
        print(f"{self.nome} {self.sobrenome}")

"""
Obs: o "sobrenome" da class ClienteVip só existe na __init__ DELE, porem ele está pegando parte dos argumentos
do super() em instancias superiores e acrescentando o sobrenome no construtor.

Resumo: "Pegado tudo o que tem criado no Pessoa e socando coisa nova (no caso o sobrenome)
"""

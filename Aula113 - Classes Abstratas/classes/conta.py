from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property  # <- Aqui estou criando para cada parámetro, assim ele retorna e não altera no __init__ principal.
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter  # <-- Esou deixando aqui apenas esa FUNC ser editável pelo User!
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):  # <- Aqui estou checando se o valor informado NÃO é Int ou Float
            raise ValueError("Saldo precisa ser númérico.")

        self._saldo = valor  # <- valor vai receber o que foi digitado.
        self.detalhes()

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito precisa ser númérico.")

        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f"Agência: {self.agencia} ", end="")
        print(f"Conta: {self.conta} ", end="")
        print(f"Saldo: R$ {self.saldo:.2f}")

    @abstractmethod
    def sacar(self, valo):
        pass

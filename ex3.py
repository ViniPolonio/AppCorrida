class ContaBancaria:
    def __init__(self):
        self.__saldo = 0.0

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def deposito(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            return False

    def imprimir_saldo(self):
        print("Saldo atual:", self.__saldo)


class ContaCorrente(ContaBancaria):
    def __init__(self, limite_saque):
        super().__init__()
        self.__limite_saque = limite_saque

    def get_limite_saque(self):
        return self.__limite_saque

    def set_limite_saque(self, limite_saque):
        self.__limite_saque = limite_saque

    def saque(self, valor):
        if valor <= self.__limite_saque and valor <= self.get_saldo():
            self.set_saldo(self.get_saldo() - valor)
            return True
        else:
            return False


class ContaPoupanca(ContaBancaria):
    def __init__(self):
        super().__init__()

    def render_juros(self, taxa):
        juros = self.get_saldo() * (taxa / 100)
        self.deposito(juros)

conta_corrente = ContaCorrente(limite_saque=1000.0)
conta_corrente.deposito(2000.0)
conta_corrente.saque(500.0)

conta_corrente.imprimir_saldo()
print("Limite possivel de saque:", conta_corrente.get_limite_saque())

conta_poupanca = ContaPoupanca()
conta_poupanca.deposito(1000.0)
conta_poupanca.render_juros(1.5)

conta_poupanca.imprimir_saldo()

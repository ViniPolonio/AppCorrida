import random

class Pessoa:
    def __init__(self, nome, idade, telefone, cpf):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.cpf = cpf

class Passageiro(Pessoa):
    def __init__(self, nome, idade, telefone, cpf):
        super().__init__(nome, idade, telefone, cpf)
        self.forma_pagamento = ""

    def solicitar_corrida(self, origem, destino, forma_pagamento):
        self.origem = origem
        self.destino = destino
        self.forma_pagamento = forma_pagamento

    def acessar_informacoes_motorista(self, motorista):
        # Método que exibe informações do motorista
        print("Informações do Motorista:")
        print("Nome:", motorista.nome)
        print("Avaliação individual do motorista:", motorista.avaliacao)
        print("Modelo de carro:", motorista.veiculo.modelo)
        print("Placa:", motorista.veiculo.placa)
        print("Ano de Fabricação:", motorista.veiculo.ano_fabricacao)
        print("Cor:", motorista.veiculo.cor)
        if isinstance(motorista.veiculo, Carro):
            print("Número de Portas:", motorista.veiculo.numero_portas)
            print("Número de Lugares:", motorista.veiculo.numero_lugares)
        elif isinstance(motorista.veiculo, Moto):
            print("Cilindradas:", motorista.veiculo.cilindradas)
        print("="*30)

    def acessar_informacoes_corridas(self, corridas):
        # Método que exibe informações das corridas do passageiro
        for corrida in corridas:
            print("Origem da corrida:", corrida.origem)
            print("Destino da corrida:", corrida.destino)
            print("Tempo de duração da corrida:", corrida.duracao)
            print("Distância percorrida:", corrida.distancia)
            print("Valor final:", corrida.valor_final)
            print("="*30)

class Motorista(Pessoa):
    def __init__(self, nome, idade, telefone, cpf, numero_licenca, veiculo, avaliacao):
        super().__init__(nome, idade, telefone, cpf)
        self.numero_licenca = numero_licenca
        self.veiculo = veiculo
        self.avaliacao = avaliacao

    def aceitar_corrida(self, passageiro, origem, destino):
        # Método que permite ao motorista aceitar uma corrida
        return Corrida(passageiro, self, origem, destino)

class Veiculo:
    def __init__(self, placa, modelo, ano_fabricacao, cor):
        self.placa = placa
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.cor = cor

class Carro(Veiculo):
    def __init__(self, placa, modelo, ano_fabricacao, cor, numero_portas, numero_lugares):
        super().__init__(placa, modelo, ano_fabricacao, cor)
        self.numero_portas = numero_portas
        self.numero_lugares = numero_lugares

class Moto(Veiculo):
    def __init__(self, placa, modelo, ano_fabricacao, cor, cilindradas):
        super().__init__(placa, modelo, ano_fabricacao, cor)
        self.cilindradas = cilindradas

class Corrida:
    def __init__(self, passageiro, motorista, origem, destino):
        self.passageiro = passageiro
        self.motorista = motorista
        self.origem = origem
        self.destino = destino
        self.duracao = random.randint(10, 30)
        self.distancia = random.randint(5, 20)
        self.valor_final = self.calcular_valor()

    def calcular_valor(self):
        # Método que calcula o valor da corrida com base na distância e duração
        taxa_quilometro = 2.5
        taxa_minuto = 0.5
        valor = self.distancia * taxa_quilometro + self.duracao * taxa_minuto
        if isinstance(self.motorista.veiculo, Carro) and self.motorista.veiculo.ano_fabricacao >= 2018 and self.motorista.veiculo.numero_portas == 4 and self.motorista.veiculo.numero_lugares >= 5 and self.motorista.avaliacao >= 4.85:
            valor *= 1.5
        return valor

class RelatorioCorridas:
    def __init__(self):
        self.corridas = []

    def adicionar_corrida(self, corrida):
        # Método que adiciona uma corrida ao relatório
        self.corridas.append(corrida)

    def resumo_corridas(self):
        # Método que retorna um resumo das corridas registradas
        resumo = []
        for corrida in self.corridas:
            resumo.append(f"Origem: {corrida.origem}, Destino: {corrida.destino}, Duração: {corrida.duracao}, Distância: {corrida.distancia}, Valor: {corrida.valor_final}")
        return resumo

# Exemplo de uso:

# Criando um objeto de carro
carro1 = Carro("ABC1234", "Fusca", 2019, "Vermelho", 4, 4)

# Criando um objeto de motorista
motorista1 = Motorista("João", 30, "999999999", "123456789", "987654321", carro1, 4.9)

# Criando um objeto de passageiro
passageiro1 = Passageiro("Maria", 25, "888888888", "987654321")

# Solicitando uma corrida pelo passageiro
passageiro1.solicitar_corrida("A", "B", "Cartão de crédito")

# Motorista aceita a corrida do passageiro
corrida1 = motorista1.aceitar_corrida(passageiro1, "Rua Poze do Rodo", "Rua Poze Bandido")

# Criando um relatório de corridas
relatorio = RelatorioCorridas()

# Adicionando a corrida ao relatório
relatorio.adicionar_corrida(corrida1)

# Exibindo as informações do passageiro
print("Informações do Passageiro:")
print("Nome:", passageiro1.nome)
print("Idade:", passageiro1.idade)
print("Telefone:", passageiro1.telefone)
print("CPF:", passageiro1.cpf)
print("="*30)

# Acessando informações do motorista pelo passageiro
passageiro1.acessar_informacoes_motorista(motorista1)

# Acessando informações das corridas pelo passageiro
passageiro1.acessar_informacoes_corridas(relatorio.corridas)
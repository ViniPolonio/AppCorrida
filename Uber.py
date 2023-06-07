class Viagem:
    def __init__(self, origem, destino, distancia_km, valor_viagem):
        self.origem = origem
        self.destino = destino
        self.distancia_km = distancia_km
        self.valor_viagem = valor_viagem

    def Origem_Uber(self):
        return f"A origem da corrida será: {self.origem}"

    def Destino_Uber(self):
        return f"O destino será: {self.destino}"

    def Distancia_Uber(self):
        return f"A distância percorrida será de: {self.distancia_km} KM"

    def Valor_Uber(self):
        return f"O valor final da viagem com desconto aplicado ficou: R${self.valor_viagem:.2f}"


class Pagamento:
    def __init__(self, forma):
        self.forma = forma

    def Forma_Pag(self):
        return f"O modelo de pagamento será: {self.forma}"


class Corrida:
    def __init__(self, viagem, tempo_minutos, pagamento):
        self.viagem = viagem
        self.tempo_minutos = tempo_minutos
        self.pagamento = pagamento

    def Calcular_Preco_Base(self):
        Preco_Base = 2 * self.viagem.distancia_km + 0.5 * self.tempo_minutos
        return Preco_Base

    def Calcular_Desconto(self):
        if self.pagamento.forma == "Pix":
            desconto = 0.1
        elif self.pagamento.forma == "Cartão":
            desconto = 0.5
        else:
            desconto = 0
        return desconto

    def Valor_Total(self):
        Preco_Base = self.Calcular_Preco_Base()
        Desconto = self.Calcular_Desconto()
        Valor_Desconto = Preco_Base * Desconto
        Valor_Final = Preco_Base - Valor_Desconto
        return Valor_Final


class Motorista:
    def __init__(self, nome, corridas_realizadas):
        self.nome = nome
        self.corridas_realizadas = corridas_realizadas

    def Adicionar_Corrida(self, corrida):
        self.corridas_realizadas.append(corrida)

    def Calcular_Total_Recebido(self):
        Valor_Total = 0
        for corrida in self.corridas_realizadas:
            Valor_Total += corrida.Valor_Total()
        return Valor_Total


viagem1 = Viagem("Joaquim Inacio de Souza", "Francisco Toczek", 3, 12.50)
pagamento1 = Pagamento("Pix")
corrida1 = Corrida(viagem1, 20, pagamento1)
motorista1 = Motorista("João Vinicius", [corrida1])
print(viagem1.Origem_Uber())
print(viagem1.Destino_Uber())
print(viagem1.Distancia_Uber())
print(pagamento1.Forma_Pag())
print(f"O valor bruto da corrida sem descontos ficou: R${corrida1.Calcular_Preco_Base()}")
print(viagem1.Valor_Uber())
print(f"O motorista {motorista1.nome} recebeu R${motorista1.Calcular_Total_Recebido():.2f} pela corrida realizada.")
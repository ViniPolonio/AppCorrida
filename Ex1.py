import datetime

class Funcionario:
    def __init__(self, nome, idade, salario):
        self.__nome = nome
        self.__idade = idade
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def aniversario(self):
        self.__idade += 1

    def ano_de_nasc(self):
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.__idade

    def aumentar_salario(self, percentual):
        aumento = self.__salario * (percentual / 100)
        self.__salario += aumento

funcionario1 = Funcionario("João", 30, 5000.0)
print("-" * 10, "DADOS DO FUNCIONÁRIO", "-" * 10)
print("Nome do funcionário:", funcionario1.get_nome())
print("Idade do funcionário:", funcionario1.get_idade())
print("Salário do funcionário:", funcionario1.get_salario())
print("Ano de nascimento:", funcionario1.ano_de_nasc())

print("-" * 10, "DADOS ATUALIZADOS", "-" * 10)
funcionario1.aumentar_salario(10)
funcionario1.aniversario()
funcionario1.set_nome("João")
print("Nome do funcionário atualizado:", funcionario1.get_nome())
print("Idade do funcionário com adicional de 1 ano:", funcionario1.get_idade())
print("Salário com adicional de 10%:", funcionario1.get_salario())

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def apresentar(self):
        print(f"Oi, meu nome é {self._nome} e tenho {self._idade} anos.")

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        self._idade = idade


class Trabalhador:
    def __init__(self, profissao, salario):
        self._profissao = profissao
        self._salario = salario

    def trabalhar(self):
        print(f"Sou um(a) {self._profissao} e estou trabalhando.")

    def get_profissao(self):
        return self._profissao

    def set_profissao(self, profissao):
        self._profissao = profissao

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario


class Estudante:
    def __init__(self, curso, instituicao):
        self._curso = curso
        self._instituicao = instituicao

    def estudar(self):
        print(f"Estou estudando {self._curso} na instituição {self._instituicao}.")

    def get_curso(self):
        return self._curso

    def set_curso(self, curso):
        self._curso = curso

    def get_instituicao(self):
        return self._instituicao

    def set_instituicao(self, instituicao):
        self._instituicao = instituicao


class EstudanteTrabalhador(Pessoa, Trabalhador, Estudante):
    def __init__(self, nome, idade, profissao, salario, curso, instituicao):
        Pessoa.__init__(self, nome, idade)
        Trabalhador.__init__(self, profissao, salario)
        Estudante.__init__(self, curso, instituicao)

    def apresentar(self):
        Pessoa.apresentar(self)
        print(f"Sou um(a) {self.get_profissao()} que trabalha como {self.get_profissao()}.")
        print(f"Estou estudando {self.get_curso()} na instituição {self.get_instituicao()}.")

    def trabalhar(self):
        Trabalhador.trabalhar(self)

    def estudar(self):
        Estudante.estudar(self)


pessoa = Pessoa("João", 25)
pessoa.apresentar()

trabalhador = Trabalhador("Engenheiro", 5000)
trabalhador.trabalhar()

estudante = Estudante("Ciência da Computação", "Universidade XYZ")
estudante.estudar()

estudante_trabalhador = EstudanteTrabalhador("Maria", 30, "Advogada", 3000, "Direito", "Universidade ABC")
estudante_trabalhador.apresentar()


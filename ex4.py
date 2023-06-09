class Pessoa:
    def __init__(self, nome, idade, endereco, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, telefone):
        self.__telefone = telefone


class Professor(Pessoa):
    def __init__(self, nome, idade, endereco, telefone, salario, disciplina):
        super().__init__(nome, idade, endereco, telefone)
        self.__salario = salario
        self.__disciplina = disciplina

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def get_disciplina(self):
        return self.__disciplina

    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina

    def dar_aula(self):
        print(f"O professor {self.get_nome()} está dando aula de {self.__disciplina}")


class Aluno(Pessoa):
    def __init__(self, nome, idade, endereco, telefone, matricula, curso):
        super().__init__(nome, idade, endereco, telefone)
        self.__matricula = matricula
        self.__curso = curso

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_curso(self):
        return self.__curso

    def set_curso(self, curso):
        self.__curso = curso

    def estudar(self):
        print(f"O aluno {self.get_nome()} está estudando o curso de {self.__curso} e possui {self.get_idade()} anos.")


pessoa = Pessoa("Vinicius", 18, "Rua Nárnia, 598", "(41) 99199-2157")
print("="*25)

print("Nome:", pessoa.get_nome())
print("Idade:", pessoa.get_idade())
print("Endereço:", pessoa.get_endereco())
print("Telefone contato:", pessoa.get_telefone())

pessoa.set_nome("Maria")
pessoa.set_idade(35)
pessoa.set_endereco("Av. Barbosa, 69")
pessoa.set_telefone("(43) 89462-6789")

print("="*25)
print("Nome:", pessoa.get_nome())
print("Idade:", pessoa.get_idade())
print("Endereço:", pessoa.get_endereco())
print("Telefone contato:", pessoa.get_telefone())

professor = Professor("Manuel", 59, "Rua Demencia, 547", "(41) 91321-6789", 2300.0, "Português")

print("Salário R$:",professor.get_salario())
print("Disciplina:", professor.get_disciplina())

print("="*25)
print("Nome:", professor.get_nome())
print("Idade:", professor.get_idade())
print("Endereço:", professor.get_endereco())
print("Telefone contato:", professor.get_telefone())
professor.set_salario(3500.0)
print("Salário R$:",professor.get_salario())
print("Disciplina:", professor.get_disciplina())



print("="*25)

aluno = Aluno("Vinicius Polonio", 18, "Rua Foda, 987", "(41) 131[1-2432", "22784801", "Engenharia de software")

print("Nome:", aluno.get_nome())
print("Idade:", aluno.get_idade())
print("Endereço:", aluno.get_endereco())
print("Telefone celular:", aluno.get_telefone())
print("Matricula:", aluno.get_matricula())
print("Curso:", aluno.get_curso())

aluno.set_matricula("2021002")
aluno.set_curso("Engenharia de software")

print("="*25)
aluno.estudar()

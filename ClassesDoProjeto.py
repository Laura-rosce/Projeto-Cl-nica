class Pacientes:

    def __init__(self, nome, cpf, telefone, indicacao, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.indicacao = indicacao
        self.verific = 0

class Endereco:
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        
class Funcionarios:

    def __init__(self, nome, cpf, telefone, salario, funcao, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.salario = salario
        self.funcao = funcao
        self.verific = 0

class Usuario:

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

        

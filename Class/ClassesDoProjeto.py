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

class Consultas:

    def __init__(self, paciente, funcionario, data, horario, valor, tipo):
        self.paciente = paciente
        self.funcionario = funcionario
        self.data = data
        self.horario = horario
        self.valor = valor
        self.tipo = tipo
        self.verific = 0
        
class Recepcionista(Usuario):
    def __init__(self, login, senha):
        super().__init__(login, senha)
        self.verific = 0

class Endereco:
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
       
    def __str__(self):
        return (f"RUA: {self.rua}\nCIDADE: {self.cidade}\nESTADO: {self.estado}")
   
class Usuario:
    def __init__(self, nome, cpf, telefone, endereco, senha):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.endereco = endereco
        self.user_name = cpf
        self.senha = senha
        self.ativo = True
       
    def __str__(self):
        return (f"LOGIN: {self.user_name}\nSENHA: *\nNOME: {self.nome}\nCPF: {self.cpf}\nTELEFONE: {self.telefone}\n{self.endereco}")

class Paciente(Usuario):
   
    def __init__(self, nome, cpf, telefone, endereco, senha, indicacao):
        super().__init__(nome, cpf, telefone, endereco, senha)
        self.indicacao = indicacao

    def __str__(self):
        return (f"{super().__str__()}\nINDICAÇÃO: {self.indicacao}\n--------------")

class Funcionario(Usuario):
    def __init__(self, nome, cpf, telefone, endereco, senha, salario, funcao,):
        super().__init__(nome, cpf, telefone, endereco, senha)
        self.salario = salario
        self.funcao = funcao
        
    def __str__(self):
        return (f"{super().__str__()}\nSALÁRIO: {self.salario}\nFUNÇÃO: {self.funcao}\n--------------")

class Clinica:
    def __init__(self, nome, cnpj,VerificarLogin):
        self.nome = nome
        self.cnpj = cnpj
        self.usuarios = []
       

    #Verifica se existe alguém cadastrado na lista de usuarios
    def tem_usuario(self):
        for usuario in self.usuarios:
            if usuario == None:
                return False
        return True

    #Verifica se já está cadastrado o user_name ou a senha
    def isUsuario(self, novo_usuario):
        posicao = 0
        if self.tem_usuario():
            for usuario in self.usuarios:
                if usuario.user_name == novo_usuario.user_name:
                    return True
                else:
                    posicao+=1
            return False
        else:
            return True
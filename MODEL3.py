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
    
    def __init__(self, nome, cnpj):
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
    
    #Verifica se cpf possui 11 caracteres 
    def caracteres_cpf_erro(self, novo_usuario):
        if len(novo_usuario.cpf) < 11 or len(novo_usuario.cpf) > 11:
            return True
        return False        
           
    #Cadastra uma pessoa no sistema, se login(cpf) e senha forem diferentes
    def cadastrar(self, novo_usuario):
        if self.isUsuario(novo_usuario):
            raise usuario_ja_cadastrado_exception
        
        if self.caracteres_cpf_erro(novo_usuario):
            raise caracteres_cpf_exception
        
        self.usuarios.append(novo_usuario)
        return True
    
    #Procura um usuario ativo e retorna ele 
    def get_usuario(self, user_name):
        for usuario in self.usuarios:
            if usuario.user_name == user_name:
                if usuario.ativo == True:
                    return usuario
        return None
    
    #Edita as informações
    def editar(self, user_name, usuario_att):
        
        usuario_desatt = self.get_usuario(user_name)
        
        if usuario_desatt != None:                       
            usuario_desatt.user_name = user_name
            usuario_desatt.senha = usuario_att.senha
            usuario_desatt.nome = usuario_att.nome
            usuario_desatt.cpf = user_name
            usuario_desatt.telefone = usuario_att.telefone
            usuario_desatt.endereco = usuario_att.endereco
            if isinstance(usuario_desatt, Paciente):
                usuario_desatt.indicacao = usuario_att.indicacao
                return True
            elif isinstance(usuario_desatt, Funcionario):
                usuario_desatt.salario = usuario_att.salario
                usuario_desatt.funcao = usuario_att.funcao
                return True
        return False
    
    #Desativa usuario, pois não exclui seus dados permanentemente 
    def excluir(self, user_name):
        
        usuario_procurado = self.get_usuario(user_name)
        if usuario_procurado != None:
            usuario_procurado.ativo = False
            return True
        return False
    
    #Guarda em uma lista, determinado tipo de usuario e retorna essa lista (só pacientes ou só funcionários, ativos ou inativos)
    def get_usuarios(self, tipo, situacao):
        lista_retorno = []
        for usuario in self.usuarios:
            if isinstance(usuario, tipo):
                if usuario.ativo == situacao:
                    lista_retorno.append(usuario)
        return lista_retorno

    #Efetua o login, testa se os dados estão corretos, ativos e qual é o tipo
    def VerificarLogin(self, user_name, senha, tipo):
        usuarios_tipo = self.get_usuarios(tipo, True)
        for usuario in usuarios_tipo:
            if usuario.user_name == user_name and usuario.senha == senha:
                return True
        return False

#TRATAMENTO DE EXCEÇÕES
class usuario_ja_cadastrado_exception(Exception): 
    pass

class caracteres_cpf_exception(Exception):
    pass

'''
class Teste:
    
    cli = Clinica("Sorriso", "12334466")
    
    endereco = Endereco("Maria", "Parelhas", "Rn")
    
    pac = Paciente("DENyse", "32155544478", "123", endereco, "insta", "111")
    print(cli.cadastrar(pac))#true
    
    pac2 = Paciente("eusou", "12345678901", "897", endereco, "whats", "222")
    print(cli.cadastrar(pac2))#true

    
    cli.VerificarLogin(pac2.user_name, pac2.senha, Paciente)#true
    
    print(cli.get_usuario(pac2))#whats

    pac2_att = Paciente(pac2.user_name, "dede", "euquero", pac2.cpf, "5698", "Face", endereco)
    print(cli.editar(pac2.user_name, pac2_att))#true

    print(cli.get_usuario(pac2.user_name))#face
'''

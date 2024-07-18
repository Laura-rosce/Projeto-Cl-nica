
from Class import *

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
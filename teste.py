from PySimpleGUI import (
    Window, Image, Input, Text, Button,
    Column, VSeparator, HSeparator, Push, popup, theme, 
    read_all_windows, Checkbox, WIN_CLOSED, Combo, Output, 
    Menu
)
from janelas_interface import * 
from MODEL3 import *
from time import sleep
import os

clinica = Clinica("Sorisso", "1256289")

#LÓGICA
login_admin = "ADMIN"
senha_admin = "ADMIN"
tipo_usuario = 0
login_efetuado = False

# Criar as janelas iniciais
janela1, janela2, janela3, janela4, janela5, janela6, janela7, janela8, janela9, janela10, janela11 = janela_inicial(), None, None, None, None, None, None, None, None, None, None


while True:
    window,event,values = read_all_windows()

     # Quando janela for fechada
    if event == WIN_CLOSED:
        break

    # Quando queremos ir para próxima janela
    if window == janela1 and event == 'Cadastre-se':
        janela2 = janela_categoria()
        janela1.hide()

    #AQUI
    if window == janela1 and event == 'Login':
        login = values['usuario']
        senha = values['senha']

        verif_Pac = clinica.VerificarLogin(login, senha, Paciente)
        verif_Func = clinica.VerificarLogin(login, senha, Funcionario)

        if verif_Pac == True:
            tipo_usuario = 1
            login_efetuado = True  
        elif verif_Func == True:
            tipo_usuario = 2
            login_efetuado = True   
        elif login == login_admin and senha == senha_admin:
            tipo_usuario = 3
            login_efetuado = True 
        else:
            popup("Login ou senha inválidos!")
            login_efetuado = False

        if login_efetuado == True and tipo_usuario == 1:
            popup('Abre a janela de login do paciente')
            #MOVIMENTO DE JANELAS
            janela9 = janela_perfil_pac('Concertar isso')
            janela1.hide()
        elif login_efetuado == True and tipo_usuario == 2:
            popup('Abre a janela de login do funcionario')
            #MOVIMENTO DE JANELAS
            janela10 = janela_perfil_fuc('Concertar isso')
            janela1.hide()
        elif login_efetuado == True and tipo_usuario == 3:
            #MOVIMENTO DE JANELA
            janela6 = janela_admin()
            janela1.hide()

        if window == janela9 and event == 'VER DADOS':
            popup('agora verr')
            #janela11 = janela_dados()
        elif window == janela9 and event == 'EDITAR DADOS':
            popup('agora edita')

        

        
               

    if window == janela2 and event == '< Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == 'Continuar >':
        if values['paciente'] == True and values['funcionario'] == True:
            popup('Ação Inválida! Escolha apenas um! ')
        elif values['paciente'] == True:
            #MOVIMENTO DAS JANELAS
            janela3 = janela_cad_Pac()
            janela2.hide()

            #PARA FILTRAR MAIS A FRENTE
            categoria = 'paciente'

        elif values['funcionario'] == True:
            #MOVIMENTO DAS JANELAS
            janela4 = janela_cad_Fun()
            janela2.hide()

            #PARA FILTRAR MAIS A FRENTE
            categoria = 'funcionario'


    if window == janela3 and event == 'Cadastrar Paciente': # JANELA CADASTRAR PACIENTE

        #MOVIMENTO DE JANELAS
        janela5 = janela_criar_login()

        #ALOCANDO DADOS 
        nome = values ['nome']
        telefone = values ['tel']
        rua = values ['rua']
        cidade = values ['cidade']
        estado = values['estado']
        indicacao = values['indic']

        popup('Paciente cadastrado com Sucesso!')
        janela3.hide()
    
    if window == janela4 and event == 'Cadastrar Funcionário': # JANELA CADASTRAR FUNCIONARIO

        #MOVIMENTO DE JANELAS
        janela5 = janela_criar_login()

        #ALOCANDO DADOS 
        nome = values ['nome']
        telefone = values ['tel']
        rua = values ['rua']
        cidade = values ['cidade']
        estado = values['estado']
        salario = values['salario']
        funcao = values['funcao']

        popup('Funcionário cadastrado com Sucesso!')
        janela4.hide()

    if window == janela3 and event == '< Voltar':
        #MOVIMENTO DE JANELAS
        janela3.hide()
        janela2.un_hide()

    if window == janela4 and event == '< Voltar':
        #MOVIMENTO DE JANELAS
        janela4.hide()
        janela2.un_hide()

    #JANELA CRIAR O LOGIN
    if window == janela5 and values['senha'] == values['senha1']: 
        if window == janela5 and event == 'Criar':

            cpf = values ['cpf']
            senha = values['senha']

            #PASSANDO PARA A CLASSE 
            endereco = Endereco(rua, cidade, estado)
            if categoria == 'paciente':
                paciente = Paciente(nome, cpf, telefone, endereco, senha, indicacao)
            elif categoria == 'funcionario':
                funcionario = Funcionario(nome, cpf, telefone, endereco, senha, salario, funcao)

            try:
                if categoria == 'paciente':
                    clinica.cadastrar(paciente)
                elif categoria == 'funcionario':
                    clinica.cadastrar(funcionario)
                #PASSANDO PARA A CLASSE O USUÁRIO
                usuario = Usuario(nome, cpf, telefone, endereco, senha)

                popup('Usuário Cadastrado com Sucesso!')

                #MOVIMENTO DE JANELAS
                janela5.hide()
                janela1.un_hide()

                 #TESTE
                print (endereco)
                print (usuario)
                print (paciente)

            except(usuario_ja_cadastrado_exception):
                popup("Usuário já cadastrado! Tente Novamente!")
            except(caracteres_cpf_exception):
                popup("Falta caracteres no CPF! Tente Novamente!") 

    elif window == janela5 and values['senha'] != values['senha1']:
        popup('Confira se as senhas são iguais!')


    #PARTE DO ADMIN

    #ABRE A JANELA DE CADASTRO DE FUNCIONÁRIO
    if window == janela6 and event == 'CADASTRAR PACIENTE': 
        #MOVIMENTO DE JANELA
        janela7 = janela_cad_paciente() 
    
    if window == janela7 and event == 'Concluir': #JANELA DE CADASTRO DE PACIENTE
        #ALOCANDO DADOS 
        nome = values ['nome']
        telefone = values ['tel']
        rua = values ['rua']
        cidade = values ['cidade']
        estado = values['estado']
        indicacao = values['indic']
        senha = values['senha'] 
        cpf = values ['cpf'] 

        usuario = Usuario(nome, cpf, telefone, endereco, senha)
        paciente = Paciente(nome, cpf, telefone, endereco, senha, indicacao)

        try:
            clinica.cadastrar(paciente)
            popup('Paciente cadastrado com Sucesso!')
            #MOVIMENTO DA JANELA
            janela7.hide()
        except(usuario_ja_cadastrado_exception):
            print("Usuário já cadastrado!")
        except(caracteres_cpf_exception):
            print("Falta caracteres no CPF! tente novamente!")
        
    elif window == janela7 and event == 'Fechar': #JANELA DE CADASTRO DE PACIENTE
        #MOVIMENTO DA JANELA
        janela7.hide()

    #ABRE A JANELA DE CADASTRO DE FUNCIONÁRIO
    if window == janela6 and event == 'CADASTRAR FUNCIONÁRIO':  
        #MOVIMENTO DE JANELA
        janela8 = janela_cad_funcionario() 

    if window == janela8 and event == 'Concluir': #JANELA DE CADASTRO DE FUNCIONÁRIO

        #ALOCANDO DADOS 
        nome = values ['nome']
        telefone = values ['tel']
        rua = values ['rua']
        cidade = values ['cidade']
        estado = values['estado']
        salario = values['salario']
        funcao = values['funcao']
        senha = values['senha'] 
        cpf = values ['cpf'] 

        usuario = Usuario(nome, cpf, telefone, endereco, senha)
        funcionario = Funcionario(nome, cpf, telefone, endereco, senha, salario, funcao)

        try:
            clinica.cadastrar(funcionario)
            popup('Funcionário cadastrado com Sucesso!')
            #MOVIMENTO DA JANELA
            janela8.hide()
        except(usuario_ja_cadastrado_exception):
            print("Usuário já cadastrado!")
        except(caracteres_cpf_exception):
            print("Falta caracteres no CPF! tente novamente!")
    elif window == janela8 and event == 'Fechar': #JANELA DE CADASTRO DE FUNCIONÁRIO
        #MOVIMENTO DA JANELA
        janela8.hide()  
   
        

    





'''

import PySimpleGUI as sg


# Criar as janelas e estilos
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input(key = 'nome')],
        [sg.Button('Continuar')]
    ]

    return sg.Window('Login', layout = layout, finalize = True)

def janela_pedido():
    window,event,values = sg.read_all_windows()
    nome = values['nome']

    sg.theme('Reddit')
    layout = [
        [sg.Text(f'Olá {nome}')],
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Pepperoni', key = 'pizza1'),
            sg.Checkbox('Pizza Frango c/ Catupiry', key = 'pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]

    ]
    return sg.Window('Montando Pedido', layout = layout, finalize = True)

# Criar as janelas iniciais
janela1, janela2 = janela_login(), None

# Criar um loop de leitura de eventos
while True:
    window,event,values = sg.read_all_windows()

    # Quando janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    # Quando queremos ir para próxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
       
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Pediu as 2 pizzas')
        elif values['pizza1'] == True:
            sg.popup('Pediu uma pizza de Peperoni')
        elif values['pizza2'] == True:
            sg.popup('Pediu uma pizza de Frando c/Catupiry')
'''
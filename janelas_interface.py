from PySimpleGUI import (
    Window, Image, Input, Text, Button,
    Column, VSeparator, HSeparator, Push, popup, theme, 
    read_all_windows, Checkbox, WIN_CLOSED, Combo, Output, 
    Menu
)

theme('Reddit')

logo = './assets/logo_dente.png'
estados = ['Acre','Alagoas','Amapá','Amazonas','Bahia','Ceará','Espírito Santo','Goiás','Maranhão','Mato Grosso','Mato Grosso do Sul','Minas Gerais','Pará','Paraíba','Paraná','Pernambuco','Piauí','Rio de Janeiro','Rio Grande do Norte','Rio Grande do Sul','Rondônia','Roraima','Santa Catarina','São Paulo','Sergipe','Tocantins','Distrito Federal']

#JANELA1
def janela_inicial(): #OKAY visual

    layout_esquerda = [
        [Image ('./assets/dente.png')]  
    ]

    layout_direita = [
    
        [Text('Usuário: ')],
        [Input(key = 'usuario')],
        [Text('Senha:')],
        [Input(password_char = '*', key = 'senha')],
        [Text()],
        [Push(), Button('Login'), Push(), Button('Cadastre-se'), Push()]
    
    ]

    layout = [
        [Column(layout_esquerda), VSeparator(), Column(layout_direita)]
    ]

    return Window('Login', icon = logo, layout = layout, finalize = True, element_justification='center')
#JANELA2
def janela_categoria(): #OKAY visual

    layout_esquerda = [
        [Push(), Checkbox('Paciente', key = 'paciente', font = 20), Push()],
        [Image ('paciente_re.png')]  
    ]

    layout_direita = [
        [Push(), Checkbox ('Funcionário', key = 'funcionario', font = 20),Push()],
        [Image ('funcionario_re.png'), Push()]
    ]

    layout = [
        [Text('')],
        [Button ('< Voltar'), Push(), Text(' <<  CATEGORIA  >>', font = 20), Push(), Button ('Continuar >')],
        [Text('')], 
        [Push(), Column(layout_esquerda), Push(), Column(layout_direita), Push()]
    ]

    return Window('Categoria', icon = logo, layout = layout, finalize = True, size = (600, 350))
#JANELA3
def janela_cad_Pac(): #OKAY visual
    
    estados = ['Acre','Alagoas','Amapá','Amazonas','Bahia','Ceará','Espírito Santo','Goiás','Maranhão','Mato Grosso','Mato Grosso do Sul','Minas Gerais','Pará','Paraíba','Paraná','Pernambuco','Piauí','Rio de Janeiro','Rio Grande do Norte','Rio Grande do Sul','Rondônia','Roraima','Santa Catarina','São Paulo','Sergipe','Tocantins','Distrito Federal']
    layout_direita = [
        [Image('car.png')]
    ]

    layout_esquerda = [
        [Text('Nome:'), Push(), Input(key = 'nome', size = (40))],
        [Text('Telefone: '),  Push(),  Input(key = 'tel', size = (40))],
        [Text('Rua: '),  Push(), Input(key = 'rua', size = (40))],
        [Text('Cidade: '), Push(), Input(key = 'cidade', size = (40))],
        [Text('Estado'), Push(), Combo(estados, key = 'estado', size = (40))],
        [Text('Indicação'),Push(), Combo(['Instagram', 'Facebook', 'Youtube', 'Amigo/Parente'], key = 'indic', size = (40))],
        [Text('')],
        [Push(), Button('Cadastrar Paciente'), Push()]
    ]

    layout = [
        [Text('')],
        [Button ('< Voltar'), Push(), Text(' CADASTRO  DE  PACIENTES ', font = 50), Push()],
        [Text('')], 
        [Column(layout_direita), Push (), VSeparator(color='white'), Push(), Column(layout_esquerda)]
    ]

    return Window('Cadastro do Paciente', icon = logo, layout=layout, finalize = True, size = (800, 500))
#JANELA4
def janela_cad_Fun(): #OKAY visual
    
    layout_direita = [
        [Image('car.png')]
    ]

    layout_esquerda = [
        [Text('Nome:'), Push(), Input(key = 'nome', size = (40))],
        [Text('Telefone: '), Push(), Input(key = 'tel', size = (40))],
        [Text('Rua: '), Push(), Input(key = 'rua', size = (40))],
        [Text('Cidade: '), Push(), Input(key = 'cidade', size = (40))],
        [Text('Salário: '), Push(), Input(key = 'salario', size = (40))],
        [Text('Estado'), Push(), Combo(estados, key='estado', size = (40))],
        [Text('Função'), Push(), Combo(['Auxiliar de Saúde bucal - ASB', 'Dentista', 'Estagiário(a)', 'Faxineiro', 'Recepcionista'], key = 'funcao', size = (40))],
        [Text('')],
        [Push(), Button('Cadastrar Funcionário'), Push()]
    ]

    layout = [
        [Text('')],
        [Button ('< Voltar'), Push(), Text('CADASTRO  DE  FUNCIONÁRIOS', font = 50), Push()],
        [Text('')],
        [Column(layout_direita), Push(),  VSeparator(color='white'), Push(), Column(layout_esquerda)]
    ]

    return Window('Cadastro do Funcionário', layout=layout, finalize = True,  size = (800, 500))
#JANELA5
def janela_criar_login(): #OKAY visual
    layout_cima = [
        [Push(), Image('confei.png'), Push()]
    ]

    layout_baixo =[
        [Push(), Text('Digite  seu CPF: ',font = 5), Push(), Input(key = 'cpf', size=(40)), Push()],
        [Push(), Text('Crie uma senha: ', font = 5), Push(), Input(key = 'senha', size=(40)), Push()],
        [Push(), Text('Confirme senha: ', font = 5), Push(), Input(key = 'senha1', size=(40)), Push()],
        [Text('')],
        [Push () , Button('Criar',size = (30), font = 10), Push()]
    ]

    layout = [
        [Text('')],
        [Text('')],
        [Push(), layout_cima, Push()],
        [Text('')],
        [Push(), layout_baixo, Push()]
    ]

    return Window('Criação de Usuário', icon = logo, layout = layout, finalize = True ,size = (800,500))

#JANELA6
def janela_admin():
    menu = [
        ['Arquivo', ['Funcionários', 'Pacientes']],
        ['Editar', ['Alterar funcionário', 'Alterar paciente']],
        ['Inserir', ['Inserir funcionário', 'Inserir paciente']],
        ['Consultar', ['Consultar funcionário', 'Consultar paciente']],
        ['Deletar', ['Excluir funcionário', 'Excluir paciente']]
    ]

    layout_cima = [
        [Image('logo.png')]
    ]

    layout_esquerda = [
        [Text('Olá, Seja Bem-Vindo(a)!', font='arial 20')],
        [Text('Informe o nome (Paciente ou Funcionário)', font='arial 12')],
        [Input(key='pesquisa', size=(50,1))],
        [Text('')],
        [Button('CONSULTAR PACIENTE', pad=(0, 10), font='arial 13 bold underline', button_color = 'gray', size = (40,2))],
        [Button('CONSULTAR FUNCIONÁRIO', pad=(0, 10), font='arial 13 bold underline', button_color = 'gray', size = (40,2))],
        [Button('CADASTRAR PACIENTE',  pad=(0, 10),font='arial 13 bold underline', size = (40,2)) ],
        [Button('CADASTRAR FUNCIONÁRIO', pad=(0, 10), font='arial 13 bold underline', size = (40,2))]
    ]

    layout_direita = [
        [Output(size = (50,20), background_color='white', font='arial 12 bold', key='saida')]
    ]

    layout_baixo = [
        [Button('Sair', size=(20),  font='arial 12', button_color='gray')]
    ]

    layout = [
        [Menu(menu, background_color = '#cccccc')], 
        [layout_cima],
        [Push(), Column (layout_esquerda), Text(' ' * 10), Column(layout_direita)],
        [Text('')],
        [layout_baixo]
    ]

    return Window ('Gerenciador de Tarefas', icon = logo, layout=layout, element_justification='center', size=(1000, 600), finalize = True)

#JANELA7
def janela_cad_paciente():

    theme ('TanBlue')
    layout_esquerda = [
        [Text('NOME:', font='arial 13', pad=(0, (0, 15)))],
        [Text('CPF:', font='arial 13', pad=(0, (0, 15)))],
        [Text('TELEFONE:', font='arial 13', pad=(0, (0, 15)))],
        [Text('RUA:', font='arial 13', pad=(0, (0, 15)))],
        [Text('CIDADE:', font='arial 13', pad=(0, (0, 15)))],
        [Text('ESTADO:', font='arial 13', pad=(0, (0, 15)))],
    ]

    layout_direita = [
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='nome')],
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='cpf')],
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='telefone')],
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='rua')],
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='cidade')],
        [Combo(estados, size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='estado')]
    ]

    layout = [
        [Text('')],
        [Text('CADASTRO DE PACIENTES', font='arial 20', pad=(0, (0, 25)))],
        [Text('')],
        [Column(layout_esquerda), Text(' ' * 5), Column(layout_direita)],
        [Button('Concluir', button_color='gray', font='arial 12', size=(10, 1), pad=(10, (20, 0)))],
        [Button('Fechar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))]
    ]

    return Window ('Cadastro de Pacientes', icon = logo, layout=layout, element_justification='center',  element_padding=(0, 0), size=(600, 550),finalize = True)

#JANELA8
def janela_cad_funcionario():
    
    theme ('TanBlue')

    funcao = ['Auxiliar de Saúde bucal - ASB', 'Dentista', 'Estagiário(a)', 'Faxineiro', 'Recepcionista']

    layout_esquerda = [
        [Text('NOME:', font='arial 13', pad=(0, (0, 15)))],
        [Text('CPF', font='arial 13', pad=(0, (0, 15)))],
        [Text('TELEFONE:', font='arial 13', pad=(0, (0, 15)))],
        [Text('RUA:', font='arial 13', pad=(0, (0, 15)))],
        [Text('CIDADE:', font='arial 13', pad=(0, (0, 15)))],
        [Text('ESTADO:', font='arial 13', pad=(0, (0, 15)))],
        [Text('SALÁRIO:', font='arial 13', pad=(0, (0, 15)))],
        [Text('FUNÇÃO:', font='arial 13', pad=(0, (0, 15)))],
    ]

    layout_direita = [
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='nome')],
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='cpf')],
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='telefone')],
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='rua')],
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='cidade')],
        [Combo(estados, size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='estado')],
        [Input(size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='salario')],
        [Combo(funcao, size=(35, 1), background_color='white', font='arial 12', pad=(0, (0, 15)), key='funcao')]
    ]

    layout = [
        [Text('')],
        [Text('CADASTRO DE FUNCIONÁRIOS', font='arial 20', pad=(0, (0, 25)))],
        [Column(layout_esquerda), Text(' ' * 5), Column(layout_direita)],
        [Button('Concluir', button_color='gray', font='arial 12', size=(10, 1), pad=(10, (20, 0)))],
        [Button('Fechar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))]
    ]

    return Window ('Cadastro de Funcionários', icon = logo, layout=layout, element_justification='center',  element_padding=(0, 0), size=(600, 550),finalize = True)

#JANELA9
def janela_perfil_pac(nome):
    menu = [
        ['Consultas',['Agendar Consulta', 'Ver Consulta']],
        ['Clínica', ['Dúvidas', 'Sobre nós']],
        ['Sair', ['Sair do perfil']]
    ]

    layout_cima = [
        [Image ('user.png'), Text(f'Seja Bem-Vindo(a) {nome}!', font='arial 20'), Push()]
    ]

    layout_esquerda =[
        [Text('')],
        [Push(), Image('dados.png'),Push()],
        [Button('VER DADOS', pad=(0, 10), font='arial 13 bold underline', size = (40,3))]   
    ]

    layout_direita = [
        [Text('')],
        [Push(), Image('edit.png'),Push()],
        [Button('EDITAR DADOS', pad=(0, 10), font='arial 13 bold underline',  size = (40,3))]
    ]

    layout_baixo = [
        [Image("logo.png")]
    ]

    layout = [
        [Menu(menu, background_color = '#cccccc')], 
        [layout_cima],
        [Text('')],
        [Column(layout_esquerda),Text(' ' * 10),Column(layout_direita)],
        [Text('')],
        [Text('')],
        [layout_baixo]
        
    ]

    return Window ('Perfil do Paciente', icon = logo, layout=layout, element_justification='center', size=(1000, 600), finalize = True)

#JANELA10
def janela_perfil_fuc(nome):
    
    menu = [
        ['Arquivo',['Gerar Arquivo', 'Salavar Arquivo']],
        ['Clínica', ['Dúvidas', 'Sobre nós']],
        ['Sair', ['Sair do perfil']]
    ]

    layout_cima = [
        [Image ('user.png'), Text(f'Seja Bem-Vindo(a) {nome}!', font='arial 20'), Push()]
    ]

    layout_esquerda =[
        [Text('')],
        [Push(), Image('dados.png'),Push()],
        [Button('VER DADOS', pad=(0, 10), font='arial 13 bold underline', button_color='Orange', size = (40,3))]   
    ]

    layout_direita = [
        [Text('')],
        [Push(), Image('edit.png'),Push()],
        [Button('EDITAR DADOS', pad=(0, 10), font='arial 13 bold underline', button_color='orange',  size = (40,3))]
    ]

    layout_baixo = [
        [Image("logo.png")]
    ]

    layout = [
        [Menu(menu, background_color = '#cccccc')], 
        [layout_cima],
        [Text('')],
        [Column(layout_esquerda),Text(' ' * 10),Column(layout_direita)],
        [Text('')],
        [Text('')],
        [layout_baixo]
        
    ]

    return Window ('Perfil do Funcionário', icon = logo, layout=layout, element_justification='center', size=(1000, 600), finalize = True)

#JANELA11
def janela_dados():
    theme ('TanBlue')

    layout_central = [
        [Output(size = (50,20), background_color='white', font='arial 12 bold', key='saida')]
    ]  

    layout = [
        [Text('')],
        [Text('SEUS DADOS', font='arial 20 bold underline', pad=(0, (0, 25)))],
        [Text('')],
        [layout_central],
        [Button('Fechar', font='arial 12', size=(8, 1), pad=(10, (20, 0)))]
    ]
    return Window ('Dados do Paciente', icon = logo, layout=layout, element_justification='center',  element_padding=(0, 0), size=(600, 600),finalize = True)


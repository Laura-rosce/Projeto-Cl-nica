from PySimpleGUI import (
    Window, Image, Input, Text, Button,
    Column, VSeparator, HSeparator, Push, popup, theme, 
    read_all_windows, Checkbox, WIN_CLOSED, Combo, Output, 
    Menu, re
)
import PySimpleGUI as sg
logo = 'logo_dente.png'

theme('Reddit')



def janela_perfil_pac():
    menu = [
        ['Consultas',['Agendar Consulta', 'Ver Consulta']],
        ['Clínica', ['Dúvidas', 'Sobre nós']],
        ['Sair', ['Sair do perfil']]
    ]

    layout_cima = [
        [Image ('user.png'), Text(f'Seja Bem-Vindo(a)!', font='arial 20'), Push()]
    ]

    layout_esquerda =[
        [Text('')],
        [Push(), Image('dados.png'),Push()],
        [Button('VER DADOS', pad=(0, 10), font='arial 13 bold underline',  size = (40,3))]
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

def janela_edit_paciente():
    
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
    return Window ('Dados do Paciente', icon = logo, layout=layout, element_justification='center', size=(600, 600), finalize = True)

janela1, janela2, janela3=  janela_perfil_pac(), None, None

while True:
    window, event, values = read_all_windows()

    if event == WIN_CLOSED:
        break

    if window == janela1 and event == 'VER DADOS':
        janela3 = janela_dados()


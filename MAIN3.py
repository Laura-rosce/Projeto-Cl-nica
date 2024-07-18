import os
from time import sleep
from MODEL3 import caracteres_cpf_exception, usuario_ja_cadastrado_exception
from Class import Funcionario, Usuario, clinica, Paciente, Endereco

while True:
    #NÃO PRECISA PQ JÁ TEM NA INTERFACE
    
    cont = 1

    while cont != 2:
        print("""
        Cadastrar....1
        Entrar.......2
        """)
        try:
            escolha = int(input("Digite sua escolha: "))
            if escolha == 1 or escolha == 2:
                cont = 2
                os.system('cls')
                sleep(1)
            else:
                print("opcao invalida")
                sleep(1)
                os.system("cls")

        except:
            print("APENAS NUMERO")
            sleep(1)
            os.system("cls")
    
    #Apenas ADMIM pode cadastrar funcionario
    if escolha == 1:
        
        nome = input("NOME: ")
        cpf = input("CPF: ")
        telefone = input("TELEFONE: ")
        rua = input("RUA: ")
        cidade = input("CIDADE: ")
        estado = input("ESTADO: ")
        indicacao = input("INDICAÇÃO: ")
        senha = input("SENHA: ")

        endereco = Endereco(rua, cidade, estado)
        usuario = Usuario(nome, cpf, telefone, endereco, senha)
        paciente = Paciente(nome, cpf, telefone, endereco, senha, indicacao)
        
        try:
            clinica.cadastrar(paciente)
            print("Cadastramento realizado com sucesso :)")
            sleep(1)
            os.system('cls')
            
        except usuario_ja_cadastrado_exception:
            print("Usuário já cadastrado")
            sleep(1)
            os.system('cls')

        except(caracteres_cpf_exception):
            print("Falta caracteres no CPF")
            sleep(1)
            os.system('cls')
            
    elif escolha == 2:
        login = input("LOGIN: ")
        senha = input("SENHA: ")
        
        verif_Pac = clinica.VerificarLogin(login, senha, Paciente)
        verif_Func = clinica.VerificarLogin(login, senha, Funcionario)

        senha_admin = "admin"  # Replace "admin" with the actual password for the admin user

        login_admin = "admin"  # Replace "admin" with the actual login for the admin user

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
            print("Login ou senha inválidos!")
            login_efetuado = False

        while login_efetuado == True:
            if tipo_usuario == 1:
                os.system('cls')
                print("""
------Bem vindo, paciente-----
    Ver seus dados.......1
    Editar seus dados....2
    Sair ................0
""") 
                opcao = int(input("Digite sua escolha: "))
                
                if opcao == 1:
                    os.system('cls')
                    print(clinica.get_usuario(login))
                    os.system('pause')
                    
                elif opcao == 2:
                    nome = input("Digite o novo nome: ")
                    cpf = login
                    telefone = input("Digite o novo telefone: ")
                    rua = input("Digite sua nova rua: ")
                    cidade = input("Digite sua nova cidade: ")
                    estado = input("Digite seu novo estado: ")
                    indicacao = input("Digite sua nova indicação: ")
                    senha = input("Digite sua nova senha: ")

                    endereco_att = Endereco(rua, cidade, estado)
                    usuario_att = Usuario(nome, cpf, telefone, endereco_att, senha)
                    paciente_att = Paciente(nome, cpf, telefone,endereco_att, senha, indicacao)
                    verif_edit = clinica.editar(login, paciente_att)

                    if verif_edit == True:
                        os.system('cls')
                        print("Paciente editado com sucesso!")
                        os.system('pause')
                    else:
                        os.system('cls')
                        print("Edição cancelada")
                        os.system('pause')
                    
                elif opcao == 0:
                    login_efetuado = False
                    os.system('cls')
                    break
                
                else:
                    print("Opção inválida")
                    os.system('pause')
                
            elif tipo_usuario == 2:
                os.system('cls')
                print("""
------Bem vindo, funcionário-----
    Ver seus dados.......1
    Editar seus dados....2
    Sair ................0
""") 
                opcao = int(input("Digite sua escolha: "))
                
                if opcao == 1:
                    os.system('cls')
                    print(clinica.get_usuario(login))
                    os.system('pause')
                    
                elif opcao == 2:
                    nome = input("Digite o novo nome: ")
                    cpf = login
                    telefone = input("Digite o novo telefone: ")
                    rua = input("Digite sua nova rua: ")
                    cidade = input("Digite sua nova cidade: ")
                    estado = input("Digite seu novo estado: ")
                    senha = input("Digite sua nova senha: ")


                    funcionario_desatt = clinica.get_usuario(login)
                    endereco_att = Endereco(rua, cidade, estado)
                    usuario_att = Usuario(nome, cpf, telefone, endereco_att, senha)
                    funcionario_att = Funcionario(nome, cpf, telefone,endereco_att, senha, funcionario_desatt.salario, funcionario_desatt.funcao)
                    verif_edit = clinica.editar(login, funcionario_att)

                    if verif_edit == True:
                        os.system('cls')
                        print("Funcionário editado com sucesso")
                        os.system('pause')
                    else:
                        os.system('cls')
                        print("Edição cancelada")
                        os.system('pause')
                    
                elif opcao == 0:
                    login_efetuado = False
                    os.system('cls')
                    break
                
                else:
                    print("Opção inválida")
                    os.system('pause')
                    
            elif tipo_usuario == 3:
                print(f"""
------Bem vindo, Administrador-----
    Cadastrar.................1
    Editar....................2
    Listar....................3
    Excluir...................4
    Sair .....................0
""") 

#FEITO

                opcao = int(input("Digite sua escolha: "))
                if opcao == 1:
                    os.system('cls')
                    print("""
    Paciente ..........1
    Funcionário .......2
    """)
                    escolha_tipo = int(input("Escolha o tipo de usuario: "))
                    os.system('cls')
                    nome = input("NOME: ")
                    cpf = input("CPF: ")
                    telefone = input("TELEFONE: ")
                    rua = input("RUA: ")
                    cidade = input("CIDADE: ")
                    estado = input("ESTADO: ")
                    endereco = Endereco(rua, cidade, estado)
                    
                    if escolha_tipo == 1:
                        indicacao = input("INDICAÇÃO: ")
                        senha = input("SENHA: ")
                
                        usuario = Usuario(nome, cpf, telefone, endereco, senha)
                        paciente = Paciente(nome, cpf, telefone, endereco, senha, indicacao)
                        
                        try:
                            clinica.cadastrar(paciente)
                            os.system('cls')
                            print("Cadastramento realizado com sucesso :)")
                            sleep(1)
                            
                        except(usuario_ja_cadastrado_exception):
                                os.system('cls')
                                print("Usuário já cadastrado")
                                sleep(1)

                        except(caracteres_cpf_exception):
                                os.system('cls')
                                print("Falta caracteres no CPF, tente novamente!")
                                sleep(1)
                                    
                    elif escolha_tipo == 2:
                        salario = input("SALÁRIO: ")
                        funcao = input("FUNÇÃO: ")
                        senha = input("SENHA: ")
                        
                        usuario = Usuario(nome, cpf, telefone, endereco, senha)
                        funcionario = Funcionario(nome, cpf, telefone, endereco, senha, salario, funcao)
                        
                        try:
                            clinica.cadastrar(funcionario)
                            os.system('cls')
                            print("Cadastramento realizado com sucesso :)")
                            sleep(1)
                            
                        except usuario_ja_cadastrado_exception:
                            os.system('cls')
                            print("Usuário já cadastrado")
                            sleep(1)

                        except caracteres_cpf_exception:
                            os.system('cls')
                            print("Falta caracteres no CPF, tente novamente!")
                            sleep(1)
                        
                    else:
                        print("Escolha inválida")
                            
                elif opcao == 2:
                    print("""
    Paciente ..........1
    Funcionário .......2
    """)
                    escolha_tipo = input("Escolha o tipo de usuário: ")
                    cpf_busca = input("Digite o cpf de busca: ")
                    
                    nome = input("Digite o novo nome: ")
                    telefone = input("Digite o novo telefone: ")
                    rua = input("Digite a nova rua: ")
                    cidade = input("Digite a nova cidade: ")
                    estado = input("Digite o novo estado: ")
                    endereco_att = Endereco(rua, cidade, estado)
                    
                    if escolha_tipo == 1:
                        indicacao = input("Digite a nova indicação: ")
                        senha = input("Digite a nova senha: ")

                        usuario_att = Usuario(nome, cpf, telefone, endereco, senha)
                        paciente_att = Paciente(nome, cpf, telefone, endereco, senha, indicacao)
                        
                        verif_edit = clinica.editar(cpf_busca, paciente_att)
                        
                    elif escolha_tipo == 2:
                        salario = input("Digite o novo salário: ")
                        funcao = input("Digite a nova função: ")
                        senha = input("Digite a nova senha: ")
                        
                        usuario_att = Usuario(nome, cpf, telefone, endereco, senha)
                        funcionario_att = Funcionario(nome, cpf, telefone, endereco, senha, salario, funcao)
                        
                        verif_edit = clinica.editar(cpf_busca, funcionario_att)
                        
                    else:
                        print("Escolha inválida")

                    if verif_edit == True:
                        print("Edição realizada com sucesso")
                    else:
                        print("Edição cancelada")
                                        
                elif opcao == 3:
                    print("""
    ------Qual tipo?--------
    Pacientes ..............1
    Funcionarios ...........2
    """)
                    tipo = int(input("Escolha: "))
                    
                    if tipo == 1:
                        tipo = Paciente
                    elif tipo == 2:
                        tipo = Funcionario
                        
                    print("""
    -----Qual situação?-----
    Ativos ................1
    Inativos ..............2
    """)                                    
                    situacao = int(input("Escolha: "))

                    if situacao == 1:
                        situacao = True
                    elif situacao == 2:
                        situacao = False
                        
                    usuarios = clinica.get_usuarios(tipo, situacao)
                    for usuario in usuarios:
                        print(f"{usuario}-------------\n")
                    
                elif opcao == 4:
                    cpf_busca = input("Digite o cpf do usuários desejado para exclusão: ")

                    verif_exclusao = clinica.excluir(cpf_busca)

                    if verif_exclusao == True:
                        print("Usuário excluído com sucesso!")
                    else:
                        print("Exclusão cancelada!")    
                    
                elif opcao == 0:
                    login_efetuado = False
                    break

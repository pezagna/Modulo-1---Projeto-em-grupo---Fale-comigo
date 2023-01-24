opcao=(1)
def sinistro(): # Sub menu. Reportar sinistro
    while True:
        print("=" *44)
        print("        Dificulity Proteção Veicular")
        print("=" *44)
        print("1. Roubo ")
        print("2. Colisão ")
        print("3. Incêndio/Desastre natural ")
        print("4. Outros ")
        print("5. Voltar ")
        print("6. Sair ")
        try :
            opcao = int(input("\n""Opção: "))
        except:
            print ("\n""Opcão inválida, tente novamente.")
            continue
        if (opcao ==1):
            roubo()  
        elif(opcao== 2):
            colisao()
        elif(opcao== 3):
            incendio()
        elif(opcao== 4):
            outros()
        elif(opcao== 5):
            break
        elif (opcao == 6):
            print("\n""Atendimento encerrado.""\n")
            exit()   
        else:
            ("\n""Opcão inválida, tente novamente.")    
def roubo(): # Sub menu. Roubo
    while True:
        try :
            cpf = int(input("Informe o seu CPF: "))
        except:
            print ("CPF inválido, tente novamente.""\n")
            continue    
        if (cpf==12345678910): # Nesta parte, o bot poderá acessar alguma lista de dados que irá validar o login de usuário e continuar com a solicitação.

            print ("\n""Solicitação enviada. Entraremos em contato imediatamente!""\n""Vá para a delegacia mais próxima para registrar o boletim de ocorrência e retorne para cadastrar o sinistro.")
            break
        else: 
            print ("\n""Usuário não encontrado. Solicite o seu plano na opcão Realizar cotação.")
            break
def colisao(): # Sub menu. Colisão
    while True:
        try :
            cpf = int(input("Informe o seu CPF: "))
        except:
            print ("CPF inválido, tente novamente.""\n")
            continue    
        if (cpf==12345678910): # Nesta parte, o bot poderá acessar alguma lista de dados que irá validar o login de usuário e continuar com a solicitação.

            print ("\n""Solicitação enviada. Entraremos em contato imediatamente!""\n""Caso não haja vítimas, leve seu veículo para um lugar seguro e retorne depois de ter realizado o registro no órgão responsável, BRAT (Polícia Militar), DAT/BAT(Polícia federal). ")
            break
        else: 
            print ("\n""Usuário não encontrado. Solicite o seu plano na opcão Realizar cotação.")
            break
def incendio(): # Sub menu. Incêndio/Destrastre natural
    while True:
        try :
            cpf = int(input("Informe o seu CPF: "))
        except:
            print ("CPF inválido, tente novamente.""\n")
            continue    
        if (cpf==12345678910): # Nesta parte, o bot poderá acessar alguma lista de dados que irá validar o login de usuário e continuar com a solicitação.

            print ("\n""Solicitação enviada. Entraremos em contato imediatamente!")
            break
        else: 
            print ("\n""Usuário não encontrado. Solicite o seu plano na opcão Realizar cotação.")
            break
def cotacao(): # Sub menu. Consultar planos
    (input("Nome: "))
    (input("E-mail: "))
    (input("Telefone: "))
    (input("Cidade\Estado: "))
    (input("Veículo (Modelo e ano): "))
    print ("\n""Solicitação enviada. Entraremos em contato imediatamente! ")
def faleconosco(): # Sub menu. Fale Conosco
    (input("Digite sua mensagem: "))
    print("\n""Mensagem enviada. Aguarde atendimento! ")
while opcao !="6": #Menu Principal
    print("=" *44)
    print("        Dificulity Proteção Veicular")
    print("=" *44)
    print("1. Reportar sinistro")
    print("2. Consultar planos")
    print("3. Dúvidas")
    print("4. Realizar cotação")
    print("5. Fale Conosco")
    print("6. Sair ")
    try :
        opcao = int(input("\n""Opção: "))
    except:
        print ("\n""Opcão inválida, tente novamente.")
        continue
    if(opcao==1):
        sinistro()
    elif(opcao==2):
        planos()
    elif(opcao==3):
        duvidas()
    elif(opcao==4):
        cotacao()  
    elif(opcao==5):
        faleconosco()
    elif(opcao==6):
        print("\n""Atendimento encerrado.""\n")
        break
    else:
        print ("\n""Opcão inválida, tente novamente.")

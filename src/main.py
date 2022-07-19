
import mysql.connector

from user import *
from navegacao import *
from pedido import *

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senhaBanco123",
  database="projetodb"
)

mycursor = mydb.cursor()

appInit = True
while(appInit):

  print("1- Login")
  print("2- Cadastrar Usuario")

  num_login = input("Selecione uma opcao (0 para encerrar o aplicativo): ")

  if num_login == "1":

    emailUser = input("Digite seu email: ")
    senhaUser = input("Digite sua senha: ")
    validacao_email = validarEmail(emailUser,senhaUser)
    print(" ")

    if validacao_email == 1:
        cpf_user = get_cpf_user(emailUser)
        print("1- Exibir Estabelecimento")
        print("2- Pesquisar Estabelecimento")
        print("3- Encerrar Aplicativo")

        num_menu = input("Selecione uma opcao: ")
          
        while num_menu == "1" or num_menu == "2":

          if num_menu == "1":

            opcoes = []
            nomeOpcoes = []
            valorOpcoes = []

            estabelecimentoEscolhido = exibirEstabelecimentos()
            print(" ")
            print("Bem vindo a",estabelecimentoEscolhido)
            print("Cardapio:")
            exibirCardapio(estabelecimentoEscolhido,opcoes)
            definirListas(opcoes,nomeOpcoes,valorOpcoes)
            print("1- Realizar Pedido")
            print("2- Sair do Estabecimento")
            print(" ")

            num = input("Selecione uma opcao: ")

            if (num == "1"):

              print(" ")
              idSolicitacao = realizarPedido(nomeOpcoes,valorOpcoes,emailUser,estabelecimentoEscolhido)
              processarPedido(idSolicitacao,cpf_user)
              exibir_pedido()
              user_escolha = input(" ")
              if (user_escolha == "SIM"):
                 print("Pedido Realizado")
              else:
                print("Saindo do aplicativo")
                num_menu = 0

            else:
              num_menu == "0"
              break
            

          elif num_menu == "2": 

            opcoes = []
            nomeOpcoes = []
            valorOpcoes = []

            estabelecimentoEscolhido = pesquisarEstabelecimentos()
            print(" ")
            print("Bem vindo a",estabelecimentoEscolhido)
            print("Cardapio: \n")
            exibirCardapio(estabelecimentoEscolhido,opcoes)
            definirListas(opcoes,nomeOpcoes,valorOpcoes)
            print("1- Realizar Pedido")
            print("2- Sair do Estabecimento")
            print(" ")

            num = input("Selecione uma opcao: ")

            if (num == "1"):

              print(" ")
              idSolicitacao = realizarPedido(nomeOpcoes,valorOpcoes,emailUser,estabelecimentoEscolhido)
              processarPedido(idSolicitacao,cpf_user)
              exibir_pedido()
              user_escolha = input(" ")
              if (user_escolha == "SIM"):
                 print("Pedido Realizado")
              else:
                print("Saindo do aplicativo")
                num_menu = 0

            else:
              num_menu == "0"
              break

        if num_menu == 3:
            validacao_email = 0
            num_login = "0"
            appInit = False    
      
    elif validacao_email == 0:
          print("Login Invalido")

    else: 
      num_login = "0"
      appInit = False
      break
  
  elif num_login == "2":
      cadastrarUsuario()

  elif num_login == "0":
      appInit = False
      print("Aplicativo Encerrado")
  else:
      print("Opcao Invalida!")

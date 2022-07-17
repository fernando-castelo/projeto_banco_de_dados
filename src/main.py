import mysql.connector
from user import *
from navegacao import *
from pedido import *
from favoritos import *

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

      print("1- Meus favoritos")
      print("2- Exibir Estabelecimento")
      print("3- Pesquisar Estabelecimento")
      print("4- Encerrar Aplicativo")

      num_menu = input("Selecione uma opcao: ")
          
      while num_menu == "2" or num_menu == "3" or  num_menu == "1":

        if num_menu == "1":
          
          while num_menu == "1":
            print("------------------Favoritos------------------")
            buscarfavoritos(emailUser, senhaUser)
            print("------------------Selecione uma Opção------------------")
            print(" 1- Selecionar estabelecimento.")
            print(" 2- Adicionar aos favorito.")
            print(" 3- Sair dos favoritos.")
            opcao_num =int(input("|-->:"))
            if opcao_num == 1:
                
              favorito_selecionado = int(input("Selecione o estabelecimento desejado: "))
              cnpj_favorito_selecionado = consultaFavorito(favorito_selecionado, emailUser, senhaUser)
              nome_favorito = converterCnpjNome(cnpj_favorito_selecionado)
              if consultaFavorito != "erro": 
                #até aqui ok, def teste. agora precisa associar esse numero do favorito selecionado.
                print("-------------------------------")
                print("Bem vindo a",nome_favorito)
                print("Cardapio:")
                exibirCardapio(nome_favorito,opcoes)
                definirListas(opcoes,nomeOpcoes,valorOpcoes)
                print("1- Realizar Pedido")
                print("2- Sair do Estabecimento")
                print("")

                num = input("Selecione uma opcao: ")

                if (num == "1"):

                  print(" ")
                  idSolicitacao = realizarPedido(nomeOpcoes,valorOpcoes,emailUser,nome_favorito)
                  valorTotal = processarPedido(idSolicitacao)
                  print("Valor Total do pedido: ", valorTotal)
                  num_menu = 0
                else:
                  num_menu == 0
                  break
                  
              else:
                print("Opção inválida, selecione um estabelecimento da lista de favoritos.")
            if opcao_num == 2:
              123
            if opcao_num == 3:  
              123
              num_menu = 0
              break
        if num_menu == "2":

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
            valorTotal = processarPedido(idSolicitacao)
            print("Valor Total do pedido: ", valorTotal)
            num_menu = 0
              

          else:
            num_menu == "0"
            break
            

        elif num_menu == "3": 

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
            valorTotal = processarPedido(idSolicitacao)
            print("Valor Total do pedido: ", valorTotal,"\n")

          else:
            num_menu == "0"
            break

        if num_menu == 4:
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

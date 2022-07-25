
import mysql.connector

from user import *
from navegacao import *
from pedido import *
from favoritos import *

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="projetobd"
)

mycursor = mydb.cursor()

appInit = True
while(appInit):
  print("------------iMenu----------------")
  print("1- Login")
  print("2- Cadastrar Usuario")

  num_login = input("Selecione uma opcao (0 para encerrar o aplicativo): ")

  if num_login == "1":

    emailUser = input("Digite seu email: ")
    senhaUser = input("Digite sua senha: ")
    validacao_email = validarEmail(emailUser,senhaUser)
    print(" ")

    while validacao_email == 1:
      cpf_user = get_cpf_user(emailUser)
      print("------------iMenu----------------")
      print("1- Meus favoritos")
      print("2- Exibir Estabelecimento")
      print("3- Pesquisar Estabelecimento")
      print("4- Encerrar Aplicativo")

      num_menu = input("Selecione uma opcao: ")
             
      while num_menu == "1":
        print("------------------Favoritos------------------")
        buscarfavoritos(emailUser, senhaUser)
        print("------------------Selecione uma Opção------------------")
        print(" 1- Selecionar estabelecimento.")
        print(" 2- Adicionar aos favorito.")
        print(" 3- Sair dos favoritos.")
        opcao_num = (input("|-->:"))
        if opcao_num == "1":

          favorito_selecionado = int(input("Selecione o estabelecimento desejado: "))
          cnpj_favorito_selecionado = consultaFavorito(favorito_selecionado, emailUser, senhaUser)
          nome_favorito = converterCnpjNome(cnpj_favorito_selecionado)
          if consultaFavorito != "erro": 
                
            opcoes = []
            nomeOpcoes = []
            valorOpcoes = []

            print(" ")
            print("Bem vindo a ", nome_favorito)
            print("Cardapio:")
            exibirCardapio(nome_favorito,opcoes)
            definirListas(opcoes,nomeOpcoes,valorOpcoes)
            print("--------------------------------")
            print("1- Realizar Pedido")
            print("2- Sair do Estabecimento")
            print(" ")

            num = input("Selecione uma opcao: ")

            if (num == "1"):
              print(" ")
              idSolicitacao = realizarPedido(nomeOpcoes,valorOpcoes,emailUser,nome_favorito)
              processarPedido(idSolicitacao,cpf_user)
              exibir_pedido()
              user_escolha = input(" ")
              if (user_escolha == "SIM"):
                print("Pedido Realizado")
            if(num == 2):
              opcao_num == "3"
          else:
            print("Opção inválida, selecione um estabelecimento da lista de favoritos.")
        if opcao_num == "2":
          estabelecimentoEscolhidolocal = exibirEstabelecimentosfavorito()
          adicionarFavorito(cpf_user, estabelecimentoEscolhidolocal)
          print("Adicionado aos favoritos.")
        if opcao_num == "3": 
          break
      
      while num_menu == "2":

        opcoes = []
        nomeOpcoes = []
        valorOpcoes = []

        estabelecimentoEscolhido = exibirEstabelecimentos()
        print(" ")
        print("Bem vindo a",estabelecimentoEscolhido)
        print("Cardapio:")
        exibirCardapio(estabelecimentoEscolhido,opcoes)
        definirListas(opcoes,nomeOpcoes,valorOpcoes)
        print("--------------------------------")
        print("1- Realizar Pedido")
        print("2- Sair do Estabecimento")
        print(" ")

        num = input("Selecione uma opcao: ")

        if num == "1":
          print(" ")
          idSolicitacao = realizarPedido(nomeOpcoes,valorOpcoes,emailUser,estabelecimentoEscolhido)
          processarPedido(idSolicitacao,cpf_user)
          exibir_pedido()
          user_escolha = input(" ")
          if (user_escolha == "SIM"):
            print("Pedido Realizado")
            break
        if num == "2":
          break     
      
      if num_menu == "3": 
        opcoes = []
        nomeOpcoes = []
        valorOpcoes = []
        estabelecimentoEscolhido = pesquisarEstabelecimentos()
        print(" ")
        print("Bem vindo a",estabelecimentoEscolhido)
        print("Cardapio: \n")
        exibirCardapio(estabelecimentoEscolhido,opcoes)
        definirListas(opcoes,nomeOpcoes,valorOpcoes)
        print("--------------------------------")
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
      if num_menu == "4":
          validacao_email = 3
          appInit = False        
    
    if validacao_email == 3:
      print("Aplicativo encerrado.")  
    
    if validacao_email == 0:
      print("Login Invalido")

  elif num_login == "2":
    cadastrarUsuario()

  elif num_login == "0":
    appInit = False
    print("Aplicativo Encerrado")
  
  else:
    print("Opcao Invalida!")

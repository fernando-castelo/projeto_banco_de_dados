
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senhaBanco123",
  database="projetodb"
)

mycursor = mydb.cursor()

def cadastrarUsuario():
  
   nome_user = input("Digite o nome do usuario: ")
   senha_user = input("Digite uma senha: ")
   cpf_user = input("Digite seu cpf: ")
   email_user = input("Digite seu email: ")
   telefone_user = input("Digite seu telefone: ")

   sql = "INSERT INTO usuario(nome, senha, cpf, email) VALUES (%s, %s, %s,%s)"
   val = (nome_user,senha_user,cpf_user,email_user)
   mycursor.execute(sql, val)

   mydb.commit()

   sql = "INSERT INTO contato(telefone, cpf) VALUES (%s, %s)"
   val = (telefone_user, cpf_user)
   mycursor.execute(sql, val)

   mydb.commit()

def pesquisarEstabelecimentos():
  estabelecimentoNome = input("Digite o nome do estabelecimento desejado: ")

  sql = "Select Nome FROM estabelecimento WHERE Nome = %s"

  mycursor.execute(sql, (estabelecimentoNome, ))
  result = mycursor.fetchall()
  
  for i in result:
    estabelecimentoEscolhido = i[0]
  return estabelecimentoEscolhido

def exibirEstabelecimentos():
  mycursor.execute("SELECT Nome FROM estabelecimento")

  result = mycursor.fetchall()

  estabelecimentos = []
  count = 1

  for i in result:
    print(count,"-", i[0])
    estabelecimentos.append(i[0])
    count += 1

  indiceEscolhido = int(input("Selecione o estabelecimento desejado: "))

  return estabelecimentos[indiceEscolhido - 1]

def validarEmail(emailUser,senhaUser):
  try:
    mycursor.execute("SELECT Email,Senha FROM usuario WHERE Email = %s AND Senha = %s", (emailUser, senhaUser))
    result = mycursor.fetchall()
    
    if (len(result) > 0):
        return 1

    else:
       return 0

  except Exception as err:
      print("couldn't connect")
      print("General error :: ", err)

def exibirCardapio(estabelecimentoEscolhido):

  sql = "Select CNPJ FROM estabelecimento WHERE Nome = %s"

  mycursor.execute(sql, (estabelecimentoEscolhido, ))
  result = mycursor.fetchall()

  for i in result:
    cnpjEscolhido = i[0]
  
  sql = "SELECT idCardapio FROM cardapio WHERE CNPJ = %s"
  mycursor.execute(sql, (cnpjEscolhido, ))
  result = mycursor.fetchall()

  for i in result:
    cardapioEscolhido = i[0]
  
  sql = "SELECT nome, valor FROM opcoes WHERE idCardapio = %s"
  mycursor.execute(sql, (cardapioEscolhido, ))
  result = mycursor.fetchall()

  count = 1
  for i in result:
    print(count,"-", i[0]," valor: ",i[1])
    opcoes.append(i)
    count += 1

def definirListas(opcoes,nomeOpcoes,valorOpcoes):
    for i in opcoes:
      nomeOpcoes.append(i[0])
      valorOpcoes.append(i[1])

def realizarPedido(nomeOpcoes,valorOpcoes,emailUser,estabelecimentoEscolhido):
  count = 1

  sql = "Select CPF FROM usuario WHERE Email = %s"

  mycursor.execute(sql, (emailUser, ))
  result = mycursor.fetchall()

  for i in result:
    cpfUser = i[0]

  sql = "Select CNPJ FROM estabelecimento WHERE Nome = %s"

  mycursor.execute(sql, (estabelecimentoEscolhido, ))
  result = mycursor.fetchall()


  for i in result:
    cnpjEstabelecimento = i[0]
  
  idSolicitacao = input("Digite o id da solicitacao: ")

  sql = "INSERT INTO solicitacao(idsolic,CPF,CNPJ) VALUES (%s, %s, %s)"
  val = (idSolicitacao,cpfUser,cnpjEstabelecimento)
  mycursor.execute(sql, val)
  
  mydb.commit()

  while True:
    item = int(input("Selecione uma opcao do cardapio (0 para finalizar pedido): "))
    if (item == 0):
      break
    else: 
      item -= 1
      nomeItem = nomeOpcoes[item]
      valorItem = valorOpcoes[item]
      quantidade = int(input("Selecione a quantidade do item: "))

      sql = "Select idopcao FROM opcoes WHERE Nome = %s"

      mycursor.execute(sql, (nomeItem, ))
      result = mycursor.fetchall()

      for i in result:
        idOpcao = i[0]

      sql = "INSERT INTO itens (idsolic,idopcao,quantidade) VALUES (%s, %s, %s)"
      val = (idSolicitacao,idOpcao,quantidade)
      mycursor.execute(sql, val)
      
      mydb.commit()

  return idSolicitacao

def processarPedido(idSolicitacao):

  idItens = []
  quantidadeItens = []
  valorItens = []
  valorTotal = 0

  sql = "Select idopcao,quantidade FROM itens WHERE idSolic = %s"

  mycursor.execute(sql, (idSolicitacao, ))
  result = mycursor.fetchall()

  for i in result:
    idItens.append(i[0])
    quantidadeItens.append(i[1])

  for i in idItens:

    sql = "Select valor FROM opcoes WHERE idopcao = %s"
    val = i
    mycursor.execute(sql, (val, ))
    result = mycursor.fetchall()

    for j in result:
      valorItens.append(j[0])

  valorItem = []
  count = 0

  for i in valorItens:
    valorItem.append(valorItens[count] * quantidadeItens[count])
    count += 1
  
  for i in valorItem: 
    valorTotal += i

  return valorTotal


appInit = True
while(appInit):

  print("1- Login")
  print("2- Cadastrar Usuario")

  num_login = input("Selecione uma opcao: ")

  if num_login == "1":

    emailUser = input("Digite seu email: ")
    senhaUser = input("Digite sua senha: ")
    validacao_email = validarEmail(emailUser,senhaUser)
    print(" ")

    if validacao_email == 1:

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
            exibirCardapio(estabelecimentoEscolhido)
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
            

          elif num_menu == "2": 

            opcoes = []
            nomeOpcoes = []
            valorOpcoes = []

            estabelecimentoEscolhido = pesquisarEstabelecimentos()
            print(" ")
            print("Bem vindo a",estabelecimentoEscolhido)
            print("Cardapio: ")
            exibirCardapio(estabelecimentoEscolhido)
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

            else:
              num_menu == "0"

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


    


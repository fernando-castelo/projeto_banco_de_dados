import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="projetobd"
)

mycursor = mydb.cursor()

def realizarPedido(nomeOpcoes,valorOpcoes,emailUser,estabelecimentoEscolhido):
  try:

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
    
    idSolicitacao = random.randrange(1,1000)

    sql = "INSERT INTO solicitacao(idsolic,CPF,CNPJ) VALUES (%s, %s, %s)"
    val = (idSolicitacao,cpfUser,cnpjEstabelecimento)
    mycursor.execute(sql, val)

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
    
  except mysql.connector.Error as error:
      mycursor.rollback()

def definirListas(opcoes,nomeOpcoes,valorOpcoes):
    for i in opcoes:
      nomeOpcoes.append(i[0])
      valorOpcoes.append(i[1])
      
def processarPedido(idSolicitacao,cpf_user):

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


  sql = "INSERT INTO pedido (valortotal,idsolic,CPF) VALUES (%s, %s,%s)"
  val = (valorTotal,idSolicitacao,cpf_user)
  mycursor.execute(sql, val)
          
  mydb.commit()

def exibir_pedido():

  sql = "SELECT \
    usuario.Nome AS nome, \
    pedido.valortotal AS valor_total \
    FROM usuario \
    INNER JOIN pedido ON pedido.CPF = usuario.CPF "
    
  mycursor.execute(sql)

  result = mycursor.fetchall()

  nome_user = result[-1][0]
  valor_total = result[-1][1]
  print(nome_user,",seu pedido ficou no valor de: ",valor_total," deseja concluir sua compra? ")
    


    

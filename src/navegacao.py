from inspect import _void
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="projetobd"
)

mycursor = mydb.cursor()

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

def exibirCardapio(estabelecimentoEscolhido,opcoesCardapio):

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
    opcoesCardapio.append(i)
    count += 1

  return opcoesCardapio

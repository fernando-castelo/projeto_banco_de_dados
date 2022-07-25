import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="projetobd"
)

mycursor = mydb.cursor()

def buscarfavoritos(emailUser,senhaUser):

  lista_cnpj = []
  lista_favoritos = []

  mycursor.execute("SELECT CPF FROM usuario WHERE Email = %s AND Senha = %s", (emailUser, senhaUser))
  result = mycursor.fetchall()
  for i in result:
    cpfuser = i[0]

  #Filtrando o cnpj de todos os favoritos pra a lista.
  sql = "SELECT CNPJ FROM favoritos WHERE CPF = %s"
  mycursor.execute(sql, (cpfuser,))
  result = mycursor.fetchall()

  for i in result:
    lista_cnpj.append(i[0])

  #A partir dessa lista de cnpj a gente pode pegar o nome desses estabelecimentos pra ficar mais organizado
  #Como so vai poder filtrar um nome por loop a gente precisa criar outro loop for dentro do fluxo
  #Pra poder da o append de todos os nomes
  for i in lista_cnpj:
    sql = "SELECT Nome FROM estabelecimento WHERE CNPJ = %s"
    mycursor.execute(sql, (i, ))
    result = mycursor.fetchall()
    for j in result:
      lista_favoritos.append(j[0])

  #Exibicao da lista de favoritos
  count = 0
  for i in lista_favoritos:
    print(count + 1,"-",lista_favoritos[count])
    count += 1

def consultaFavorito(favorito_selecionado, emailUser, senhaUser):

  cnpj = []

  mycursor.execute("SELECT CPF FROM usuario WHERE Email = %s AND Senha = %s", (emailUser, senhaUser))
  result = mycursor.fetchall()
  for i in result:
    cpfuser = i[0]
 
  sql="SELECT CNPJ FROM favoritos WHERE CPF = %s"
  mycursor.execute(sql, (cpfuser,))
  result = mycursor.fetchall()
 
  count = 0
  valor_de_retorno = 0
  for i in result:
    cnpj.append(i[0])
    
     
    if len(cnpj)==favorito_selecionado:
      valor_de_retorno = cnpj[count] 
      return valor_de_retorno     
    count +=1

def converterCnpjNome(cnpj_favorito_selecionado):
  sql = "Select Nome FROM estabelecimento WHERE CNPJ = %s"

  mycursor.execute(sql, (cnpj_favorito_selecionado, ))
  result = mycursor.fetchall()

  for i in result:
    nomeEscolhido = i[0]

    return nomeEscolhido

def adicionarFavorito(cpf_user , cnpj):
#Inserindo novo favorito no banco com dados obtidos de exibirEstabelecimentosfavoritos 
# e get_cpf_user.
 sql = "INSERT INTO favoritos(CPF, CNPJ) VALUES (%s, %s)"
 val = (cpf_user , cnpj)

 mycursor.execute(sql, val)


def exibirEstabelecimentosfavorito():
  #Exibe os Nomes dos Estabelecimentos para o Usuário.
  mycursor.execute("SELECT Nome FROM estabelecimento")

  result = mycursor.fetchall()

  estabelecimentos = []
  count = 1
  print("------------- Adicionar aos favoritos------------")
  for i in result:
    print(count,"-", i[0])
    estabelecimentos.append(i[0])
    count += 1
  #Consulta os CNPJ sem exibir
  mycursor.execute("SELECT CNPJ FROM estabelecimento ORDER BY CNPJ DESC")

  result = mycursor.fetchall()

  cnpj = []
  count2 = 1

  for i in result:
    cnpj.append(i[0])
    count2 += 1
  #O usuário escolhe o estabelecimento
  indiceEscolhido = int(input("Selecione o estabelecimento desejado: "))
  return cnpj[indiceEscolhido - 1]
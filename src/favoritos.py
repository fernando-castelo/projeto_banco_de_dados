import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senhaBanco123",
  database="projetodb"
)

mycursor = mydb.cursor()

def buscarfavoritos(emailUser,senhaUser):

  lista_cnpj = []
  lista_favoritos = []

  mycursor.execute("SELECT CPF FROM usuario WHERE Email = %s AND Senha = %s", (emailUser, senhaUser))
  result = mycursor.fetchall()
  for i in result:
    cpfuser = i[0]

  #Filtrando o cnpj de todos os favoritos pra a lista,teu codigo tava pegando so um.
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

  mycursor.execute("SELECT CPF FROM usuario WHERE Email = %s AND Senha = %s", (emailUser, senhaUser))
  result = mycursor.fetchall()
  for i in result:
    cpfuser = i[0]

  sql="SELECT CNPJ FROM favoritos WHERE CPF = %s"
  mycursor.execute(sql, (cpfuser,))
  result = mycursor.fetchall()
  for i in result:
    cnpj = i[0]
  
  sql="SELECT CNPJ FROM estabelecimento WHERE CNPJ = %s"

  mycursor.execute(sql, (cnpj, ))
  result = mycursor.fetchall()
  favorito_selecionado -= 1
  try:
    for a in result:
      if True==(a[favorito_selecionado]):
          return a
  except Exception as err:
    erro = "erro"
    return erro

def converterCnpjNome(cnpj_favorito_selecionado):
  sql = "Select Nome FROM estabelecimento WHERE CNPJ = %s"

  mycursor.execute(sql, (cnpj_favorito_selecionado, ))
  result = mycursor.fetchall()

  for i in result:
    nomeEscolhido = i[0]

    return nomeEscolhido
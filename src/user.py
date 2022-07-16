import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="senhaBanco123",
  database="projetodb"
)

mycursor = mydb.cursor()

def cadastrarUsuario():
  try: 
   nome_user = input("Digite o nome do usuario: ")
   senha_user = input("Digite uma senha: ")
   cpf_user = input("Digite seu cpf: ")
   email_user = input("Digite seu email: ")
   telefone_user = input("Digite seu telefone: ")

   sql = "INSERT INTO usuario(nome, senha, cpf, email) VALUES (%s, %s, %s,%s)"
   val = (nome_user,senha_user,cpf_user,email_user)
   mycursor.execute(sql, val)

   sql = "INSERT INTO contato(telefone, cpf) VALUES (%s, %s)"
   val = (telefone_user, cpf_user)
   mycursor.execute(sql, val)

   mydb.commit()

  except mysql.connector.Error as error:
     mycursor.rollback()

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
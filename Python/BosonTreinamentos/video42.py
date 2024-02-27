#scrip para conexão com o mysql 

import mysql.connector

con = mysql.connector.connect(host='localhost', database = 'nome do banco', user='root', password='senha do banco')

#verificando se está conectado ao banco e retornando o status do servidor, trazendo uma consulta

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado o servidor Mysql: ", db_info)
    cursor = con.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print('Conectado ao banco de dados ', linha)

if con.is_connected():
    cursor.close()
    con.close()
    print("Conexão com o Mysql encerrada")


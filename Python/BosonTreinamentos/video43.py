#Script para realizar consulta ao banco de dados Mysql 

import mysql.connector
from mysql.connector import Error


try:
    conexao = mysql.connector.connect(host ='localhost', database='NOME DO BANCO', user='root', password='SENHA DO BANCO')

    consulta_sql = "select * from tabel_do_banco"
    cursor = conexao.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Número total de registros retornados: ", cursor.rowcount)

    print('\nMostrando os autores cadastrados')
    for linha in linhas:
        print('ID:', linha[0])
        print('Nome:', linha[1])
        print("Sobrenome:", linha[2])

except Error as e:
    print('Erro ao acessar tabela')
finally:
    if (conexao.is_connected()):
        conexao.close()
        cursor.close()
        print('Conexão ao Mysql encerrada')
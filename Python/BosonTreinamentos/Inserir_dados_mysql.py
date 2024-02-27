#inserir dados fornecidos pelo usuário em uma tabela do mysql 


#script para inserir dados em uma tabela Mysql 

import mysql.connector
from _mysql_connector import Error


print('Rotina para cadastros de produtos em BD')
print('Entre com os dados conforme solicitado')

idProd = input('ID do produto: ')
NomeProd = input("Nome do Produto: ")
precoProd = input('Preço: ')
quantProd = input('Quantidade: ')

dados = idProd + ',\'' + NomeProd + '\',' + precoProd + ',' + quantProd + ')'

declaracao = """INSERT INTO tbl_produtos
(idProduto, NomeProduto, Preco, Quantidade)
VALUES ("""

sql = declaracao + dados

try: 
    #Criar conexão com o banco de dados
    conexao =mysql.connector.connect(host='localhost', database='banco', user='root', password='SENHA DO BANCO')

    inserir_produtos = sql
    
    cursor = conexao.cursor()
    cursor.execute(inserir_produtos)
    conexao.commit()
    print(cursor.rowcount, 'Registros inseridos na tabela!')
    cursor.close()

except Error as erro:
    print("Falha ao inserir dados Mysql: ()".format(erro))

finally:
    if (conexao.is_connected()):
        cursor.close()
        cursor.close()
        print('Conexão ao Mysql encerrada!')
        
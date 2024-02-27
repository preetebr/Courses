
#script para inserir dados em uma tabela Mysql 

import mysql.connector
from _mysql_connector import Error

try: 
    #Criar conexão com o banco de dados
    conexao =mysql.connector.connect(host='localhost', database='banco', user='root', password='SENHA DO BANCO')

    inserir_produtos = """INSERT INTO tbl_produtos
                            (idProduto, NomeProduto, Preco, Quantidade)
                            VALUES
                            (1, 'Camera', 850.00,5)
                            (2, 'Monitor', 630.00,7)
                            (3, 'Reogio', 570.00,10)
                        """
    
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
        
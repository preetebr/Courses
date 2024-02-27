#Scrip para criação de tabela em um banco Mysql com Python

import mysql.connector

try: 
    #Criar conexão com o banco de dados
    conexao =mysql.connector.connect(host='localhost', database='banco', user='root', password='SENHA DO BANCO')

    #declarção SQL a ser executada
    criar_tabela_sql = """CREATE TABLE tbl_produtos (
                                idProduto int(11) NOT NULL,
                                NomeProduto VARCHAR(70) NOT NULL,
                                Preco FLOAT NOT NULL,
                                Quantidade TINYINT NOT NULL,
                                PRIMARY KEY (IdPorduto))"""

    #Criar cursor e executar SQL no banco de dados
    cursor = conexao.cursor()
    cursor.execute(criar_tabela_sql)
    print("Tabela de Produtos criada com sucesso!")

except mysql.connector.Error as erro:
    print('Falha ao criar tabela no Mysql: ()'.format(erro))

finally:
    if(conexao.is_connected()):
        cursor.close()
        conexao.close()
        print('Conexão ao Mysql finalizada.')


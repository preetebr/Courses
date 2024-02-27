#Testando os métodos read() readline() readlines()

print('Teste de abertura de arquivos em Python')
print('Tentando abrir um arquivo de texto armazenado no PC:\n')

manipulador = open('D:\Python\BosonTreinamentos\Arquivo.txt', 'r', encoding='utf8')

for linha in manipulador:
    linha = linha.rstrip()
    print(linha)
manipulador.close()


print('\nContando as linhas do arquivo de texto analisado:\n')
contador = 0 
arq = open('D:\Python\BosonTreinamentos\Arquivo.txt', 'r', encoding='utf8')
for linha in arq:
    contador = contador +1
print("Número de linhas no arquivo: ", contador)
arq.close()

print('\nRetornando somente as linhas que possuem a palavra Python:\n')
arq = open('D:\Python\BosonTreinamentos\Arquivo.txt', 'r', encoding='utf8')
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if 'Python' in linha:
        contador = contador + 1 
        print(linha)
print("\nForam retornadas", contador, 'linhas')
arq.close()

print('\nRetornando somente as linhas que possuem a palavra pesquisada:\n')
palavra = input('Digite a palavra para busca: ')
arq = open('D:\Python\BosonTreinamentos\Arquivo.txt', 'r', encoding='utf8')
contador = 0
for linha in arq:
    linha = linha.rstrip()
    if palavra in linha:
        contador = contador + 1 
        print(linha)
print("\nForam retornadas", contador, 'linhas')
arq.close()
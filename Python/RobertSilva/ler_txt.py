arquivo = open('leitura.txt')

#print(arquivo.read())
#print(type(arquivo.read()))

linhas = arquivo.readlines()
print(linhas)
print(type(linhas))

for linha in linhas:
    print(linha.replace('\n',''))
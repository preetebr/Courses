arquivo = open('escrita.txt', 'w')

for valor in range(0,11):
    linha = 'linha%s\n' %valor
    print('Escrevendo linha %s' %linha)
    arquivo.write(linha)
    
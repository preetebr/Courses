import csv

arquivo = open('escrita.csv', 'w', newline='', encoding='utf-8')
write = csv.writer(arquivo, delimiter=';')
cabecalho = ['Nome', 'Idade', 'Situacao']
write.writerow(cabecalho)


funcionario1 = ['Joao', '25', 'ativo']
print('Escrevendo linha 1')
write.writerow(funcionario1)
funcionario2 = ['Kelvyn', '29', 'Aposentado']
print('Escrevendo linha 2')
write.writerow(funcionario2)
funcionario3 = ['Cleber', '35', 'Velho']
print('Escrevendo linha 3')
write.writerow(funcionario3)

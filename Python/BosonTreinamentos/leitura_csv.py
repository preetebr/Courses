import csv

with open('elementos.csv', mode='r') as arq:
    leitor = csv.reader(arq, delimiter=',')
    linhas = 0
    for coluna in leitor:
        if linhas == 0:
            print(f'Colunas: {" ".join(coluna)}')
            linhas += 1
        else:
            print(f'\tElemento {coluna[0]} é o {coluna[1]}, de símbolo {coluna[2]}.')
            linhas += 1
    print(f'Lidas {linhas} linhas.')


   
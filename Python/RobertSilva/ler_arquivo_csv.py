import csv

arquivo = csv.reader(open('leitura.csv'), delimiter=';')
for [nome_host, ip, id_grupo, id_template] in arquivo:
    print('{} - {} - {} - {}'.format(nome_host,ip, id_grupo, id_template))
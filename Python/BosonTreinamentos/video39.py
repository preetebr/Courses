#método arg parse 


#Para rodar é necesário executar na linha de comando, chamando todo o diretório do arquivo e passando os argumentos de largura e comprimento. 
# -l (largura)
# -c (comprimento)
#python .\Python\BosonTreinamentos\video39.py -l 10 -c 15

import argparse

parser = argparse.ArgumentParser(description='Calcular área de um terreno')

# Adicionar os argumentos posicionais com o add_argument
parser.add_argument('-l','--largura', type=int, help='Largura do terreno')
parser.add_argument('-c','--comprimento', type=int, help='comprimento do terreno')


args = parser.parse_args()

def calcula_area(largura, comprimento):
    area = largura * comprimento
    return area

if __name__=='__main__':
    print('A area do terreno é de: %s m2' %calcula_area(args.largura, args.comprimento))


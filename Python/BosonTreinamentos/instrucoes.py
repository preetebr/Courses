if __name__ == '__main__':
    lista = [2,4,5,8,10,12,14]
    for n in lista:
        if n % 2 != 0:
            print('Um número impar foi ignorado')
            #break   - Para a execução
            continue #- Continua a execução, informado o impar na lista
        else:
            print(n)
    else:
        print('Nenhum número impar foi encontrado!')
    
    def calcula(x):
        pass   #ignora a função para permitir o código de rodar
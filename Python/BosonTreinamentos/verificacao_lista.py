
#Verificar se uma lista está vazia com Python

lista_desejada = []
lista_vazia = []
#Modo 1 len()

if len(lista_desejada) == 0:
    print('A lista está vazia')
else:
    print('A lista não está vazia')

#comparação com lista vazia
if lista_desejada == lista_vazia:
    print('A lista está vazia')
else:
    print('A lista não está vazia')

#Operador lógico NOT

if not lista_desejada:
    print('A lista está vazia')
else:
    print('A lista não está vazia')
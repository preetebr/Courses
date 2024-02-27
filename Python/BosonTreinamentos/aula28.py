# def listar_itens(w,x,y,z):
#     print(w,x,y,z)

# lista = [21,22,23,24]
# #listar_itens(lista)

# listar_itens(*lista) #desempacotar antes de passar o argumento

#Empacotar os itens

def somar(*args):
    soma = 0
    for i in range(0, len(args)):
        soma += args[i]
    return soma

#Testando
print(somar(1,2,3,4,5,6,7,8,9,10))
print(somar(77, 23))

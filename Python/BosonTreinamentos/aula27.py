def contar (valor=11, caractere='+'):
    for i in range(1, valor):
        print(caractere)
# contar()
# print("Passando um caractere diferente: ")
# contar(caractere="&")
# print("Passando um valor diferente: ")
# contar(valor=5)
# print("Tentando passar os parametros fora de ordem:")
# contar('#',7)

print("Passando os parametros fora de ordem, nomeados: ")
contar(caractere="#", valor=7)

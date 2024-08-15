"""
Tipo Float

Casas decimais
O separador de casas decimais na programação é o ponto e não a vírgula.

"""

#Errado
# valor=1,44

#Certo
valor = 1.44
print(valor)
print(type(valor))



#Possível
valor1, valor2 = 1, 44
print(valor1)
print(valor2)
print(type(valor1))
print(type(valor2))

#podemos converter um float para int
res = int(valor)
print(res)
print(valor)
print(type(res))


#Podemos trabalhar com números complexos
variavel = 5j
print(type(variavel))
res1 = variavel ** 2
print(res1)





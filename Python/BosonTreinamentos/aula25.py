def mensagem ():
    print('Boson Treinamentos em TI')

mensagem()

x = 5
y = 6

def soma(a,b):
    return a + b

c = soma(x, y)
print(c)

###################################################
valores = [1,2,3,4,5]

def quadrado(valores):
    quadrados = []
    for x in valores:
        quadrados.append(x**2)
    return quadrados

resultados = quadrado(valores)

for y in resultados:
    print(y)


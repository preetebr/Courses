

numeros = [2,3,4,5,6]
letras = ['a' , 'b' , 'c' , 'd', 'e']



itens = [['item1' , 'item2'] , ['item3', 'item4']]

numeros.extend(letras)
print(numeros)

print(itens[1])

produtos = ['laranja' , 'banana' , 'arroz', 'feijao']


item, *outros= produtos


print(item)
print(outros)

valores = [20,30,45,55,67]
for real in valores:
    print(f' Valor do produto: R${real}')

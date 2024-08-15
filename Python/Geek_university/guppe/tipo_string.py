"""
Tipo String

Em Python, um dado é considerado do tipo tipo string sempre que:
- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True'
- Estiver em aspas duplas
- Estiver entre aspas simples triplas
- Estiver entre aspas duplas triplas """"""


"""

nome = "Geek University"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome.upper())
print(type(nome))

nome = "Geek University"
print(nome[0:4]) #slice de string
print(nome[5:15])
print(nome.split())

#[::-1] Inverte os elementos, imprimindo de forma invertida
print(nome[::-1])













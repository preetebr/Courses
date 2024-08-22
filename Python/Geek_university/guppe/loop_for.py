"""
Loop for:  Estrutura de repetição
for: uma dessas estrutura

Python

for item in interavel:
    // exec do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
String > nome = 'Geek'

- Lista:
    lista = [1, 3, 5, 7, 9]

- range:
    numeros = range(1, 10)


"""
nome = 'Geek'
lista = [ 1, 3, 5, 7, 9]
numero = range(1, 10) #Temos que transformar em uma lista


#exemplo for 1
for letra in nome:
    print(letra)

#exemplo for 2 ( iterando sobre lista)
for numero in lista:
    print(numero)

"""
range(valor_inicial, valor_final)

obs: O valor final não é inclusive.
1 - 9, 10 não entra
"""
#exemplo de for 3 (iterando sobre range)
for numero in range(1, 10):
    print(numero)


for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _,letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantidade de loop: '))

for n in range(1, qtd + 1):
    print(f'Imprimindo {n}')
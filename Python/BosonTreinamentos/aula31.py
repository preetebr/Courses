#Modulo principal

import modfuncoes
import random

modfuncoes.mensagem()

# numero = int(input('Digite um número inteiro: '))
n = random.randint(1,10)


print("Calculando o fatorial do número: ")
#fat = modfuncoes.fatorial(numero)
fat = modfuncoes.fatorial(n)
print("O fatorial de ", n ,'é', fat)


print("Calculando a sequencia de fibonacci:")
#fib = modfuncoes.fibo(numero)
fib = modfuncoes.fibo(n)
print("O fibonacci é: ", fib)
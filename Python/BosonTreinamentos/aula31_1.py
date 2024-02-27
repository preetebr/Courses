#Módulo principal
from modfuncoes import fatorial, mensagem, fibo

mensagem()

numero = int(input('Digite um número inteiro: '))

print('Calculando o fatorial de número:')
fat = fatorial(numero)
print("O fatorial é: ", fat)

print('Exibindo a série de fibonacci até o número: ')
fib = fibo(numero)
print('Série de fibonacci:', fib)
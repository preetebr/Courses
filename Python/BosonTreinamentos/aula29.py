#Fatoração
def fatorial (numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero -1)



x = int(input('Digite um numero para calcular o fatorial: '))
res = fatorial(x)
print('O fatorial de %d é: %d' % (x,res)) 


#Fibonacci recursivo 

def fibonacci (num):
    if num <= 1:
        return num
    else: 
        return fibonacci(num -1) + fibonacci(num -2)

x = int(input("Digite um número para calculo de Fibonacci: "))
res = fibonacci(x-1)

print('O fibonacci de %d é %d' % (x, res))
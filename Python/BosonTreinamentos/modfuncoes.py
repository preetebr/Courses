#Módulo com as funções variadas

#Função que exibe mensagem de boas-vindas

def mensagem():
    print("Boson Treinamentos em TI\n")

#Funçõo para cálculo do fatorial de um número
def fatorial(numero):
    if numero < 0:
        return "Digite um valor maior ou igual a zero"
    else:
        if numero == 0 or numero == 1:
            return 1
        else:
            return numero * fatorial(numero - 1)

#Função para retornar uma série de Fibonacci até um valor x: 

def fibo(n):
    resultado = [0]
    a, b = 0 , 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado
    

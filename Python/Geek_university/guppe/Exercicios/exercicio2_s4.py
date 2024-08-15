"""
Faça um programa que leia um número inteiro, fornecido pelo usuário.
Se esse número for positivio, calcule a raiz quadrada do número e apresente-o.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido

"""
from math import sqrt
numero = int(input('Digite um número: '))

if numero > 0:
    novo = sqrt(numero)
    print(novo)
else:
    print('Esse número é inválido')
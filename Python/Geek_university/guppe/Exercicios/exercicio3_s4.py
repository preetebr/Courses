
"""
Faça um programa que recebe um número inteiro e informe se este número é par ou impar.

"""
numero = int(input("Digite um número: "))
restante = numero % 2


if restante == 0:
    print('Esse número é Par')
else:
    print('Número impar')
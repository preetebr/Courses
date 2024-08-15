"""
Escopo de variváveis.

Dois casos de escopo:
1 - variváveis globais
    - variaveis globais são reconhecidas, seu escopo compreende, todo o programa

2 - variáveis locais
     - são reconhecidas apenas no bloco onde foram declaradas, seu escopo está limitado ao bloco onde foi declarado


Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_variavel

python é uma linguagem de tipagem dinâmica. Isso significa que ao declarar uma variável, nós colocamos o tipo de dados dela.
Este tipo é inferido ao atribuírmos o valor a mesma.


"""
#Variável Global
numero = 42
print(numero)
print(type(numero))

#Varivável local:
# varivável novo está declarada localmente dentro do bloco IF.
numero = 2
if numero > 10:
    novo = numero + 10
    print(novo)
else:
    novo = numero + 2

print(novo)






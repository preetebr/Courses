"""
Tipo Booleano

Algebra Booleana, criado por George Boole

2 constante, Verdadeiro ou Falso

True - Verdadeiro
False - False
s
obs: sempre com a inicial maiúscula.

Errado:
true, false

Certo:
True, False
"""


ativo = True
print(ativo)

"""
Operações básicas
"""

#Negação (not):
"""
Fazendo a negação, se o valor for booleano for verdadeiro o resultado será falso
Se for falso o resultado será verdadeiro. Ou seja, sempre o contrário.
"""

print(not ativo)
logado  = False
#Ou (or)
"""
É uma operação binária, depende de dois valores, um ou outro deve ser verdadeiro
True or True = True
True or False = True
False or True = True
False or False = False
"""

print(ativo or logado)

#E (and)
"""
Também é uma operação binária, dependendo de dois valores. Ambos os valores devem ser verdadeiros
True or True = True
True or False = False
False or True = False
False or False = False
"""












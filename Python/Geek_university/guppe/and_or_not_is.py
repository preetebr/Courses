"""
Estruturas lógicas: And, Or, Not, Is

Operadores unário:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:
Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False e vice-versa
Para o 'is', o valor é comparado com o segundo.


"""
ativo = True
logado = False

if ativo and logado:
    print('Bem-vindo ao sistema')
else:
    print('Você precisa ativar sua conta, Acesse seu e-mail.')

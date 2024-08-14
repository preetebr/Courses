
"""
Recebendo dados do usuário.

input() -> Todo dado recebido via input é do tipo String

String é tudo que estiver entre:
- Aspas simples s'
- Aspas duplas "
- Aspas simples triplas '''
- Aspas duplas triplas """ """
"""


# Entrada de dados
#print("Qual o seu nome? ")
nome = input('Qual o seu nome? ')

#Print antigo 2.x
#print('Seja bem-vindo(a) %s' % nome)

#print moderno 3.x
#print('Seja bem vindo(a) {0}'.format(nome))

#Print 'mais atual' 3.7x
print(f'Seja bem vindo(a) {nome}')

#print('Qual sua idade: ')
idade = int(input("Qual a sua idade? "))
# Processamento



# Saída
#Print antigo 2.x
#print('A %s tem %s anos' % (nome, idade))

#print moderno 3.x
#print('A {0} tem {1} anos'.format(nome, idade))


#Print 'mais atual' 3.7x
print(f'A {nome} tem {idade} anos')

#int(idade) => cast
#Cast é a conversão de um tipo de dado para outro.
print(f'A {nome} nasceu em {2024 - int(idade)}')





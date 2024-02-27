minha_tupla = () #tupla vazia
meu_dicionario = {} #dicionário vazio
meu_conjunto = set() #Conjunto vazio

minha_tupla = ('Kelvyn', 'Pedro', 'Paulo')
print(minha_tupla)
print(minha_tupla[1])

for nome in minha_tupla:
    print(nome)
print('')

print('Dicionario')
meu_dicionario= {'nome': 'Jose', 'idade': 27}
print(meu_dicionario['nome'])
print(meu_dicionario['idade'])
meu_dicionario['idade'] = 28
print(meu_dicionario['idade'])
meu_dicionario['status'] = 'Ativo'
print(meu_dicionario)
lista_notas = [7.8, 8.4, 8.7, 9.5]
meu_dicionario['notas'] = lista_notas
print(meu_dicionario)
print(meu_dicionario['notas'])
print('')

print('Conjunto')
nomes = ['Kelvyn', 'Robert', 'Felipe', 'Paulo']
print(nomes)
meu_conjunto = set()
meu_conjunto = {'Kelvyn', 'Robert', 'Felipe', 'Paulo'}
for nome in nomes:
    meu_conjunto.add(nome)

print(meu_conjunto)
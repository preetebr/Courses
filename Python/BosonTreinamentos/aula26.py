var_global = "Boson treinamentos"
def escreve_texto():
    global var_global
    var_global= "Planeta Unix"
    var_local = 'Fabio Reis'
    print('Variavel Global: ', var_global)
    print('Variavel Local: ', var_local)

print("Executando a função escreve_texto: ")
escreve_texto()
print("Tentando acessar as variaveis diretamente: ")
print('Variavel Global: ', var_global)




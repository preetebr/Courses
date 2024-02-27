#Criando e escrevendo em arquivos de texto (modo 'w' = write)


arquivo = open('arq01.txt','w')
arquivo.write("Boson treinamentos\n")
arquivo.write("arquivo criado por Kelvyn\n")
arquivo.write('É isso ai pessoal\n')
arquivo.close()


#Lendo o arquivo criado:
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()

#acrescentado texto ao arquivo criado, usando o modo 'a'

print('\n')
texto = input('Digite uma frase para acrescentar ao arquivo:\n')
arquivo = open('arq01.txt', 'a')
arquivo.write(texto + '\n')
print("operação concluida" + arquivo.name + " usando o modo acrescentar 'a' ")
arquivo.close()

print('\nTexto alterado:')
arquivo = open('arq01.txt', 'r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()
#Testando os métodos read() readline() readlines()


import os


arquivo = 'D:\Python\BosonTreinamentos\Arquivo.txt'
if os.path.exists(arquivo):
    manipulador = open(arquivo, 'r')
else:
    print(f'O arquivo "{arquivo}" não foi encontrado.')


manipulador = open('D:\Python\BosonTreinamentos\Arquivo.txt', 'r', encoding='utf8')

print('\nMétodo read():\n')
print(manipulador.read())


manipulador.seek(0) #Volta para o inicio do arquivo

print("\nMétodo readline():\n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0)

print("\nMétodo readlines():\n")
print(manipulador.readlines())

manipulador.close()


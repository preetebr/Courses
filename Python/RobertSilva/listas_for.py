notas = [7.0, 8.5, 8.4, 3.0]
print('lista completa: {}'.format(notas))
print('Primeiro indice: {}'.format(notas[0]))
print('Ultimo indice: {}'.format(notas[-1]))#ultimo elemento da lista
print('')
print('Operações com listas')
notas.append(9.2) #Adicionar nota
print(notas)
notas.remove(3.0) #removendo uma nota
print(notas)
notas.insert(3, 8.5) #inserindo uma nota na posição 3
print(notas)
notas[0] = 9.8 #alterando uma nota
print(notas)
print('')
print('Funções utilizadas com listas')
print('Tamanho da lista: {}'.format(len(notas)))
print("quantidade de elementos 8.5 na lista: {}".format(notas.count(8.5)))

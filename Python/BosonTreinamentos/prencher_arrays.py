#Preencher arrays com valores especificos e aleatórios 

import numpy as np

#Criar um array com os números pares de 0 a 100

pares = np.array([n for n in range(0,101,2)])
print(pares)
print('')


#Preencher arrays com zeros, uns ou valores especificos 
#criar array com 10 elementos iguais a 0
print(np.zeros(10))
print('')

#Criar arrays com 15 elementos iguais a 1 e inteiros
print(np.ones(15))

print(np.ones(15, dtype=int))
print('')

#criar arrays com 8 elementos iguais a 12 int
print(np.full(8,12)) #primeiro argumento: núm de elementos
print('')

#Criar arrays com 10 elemntos iguais a 0, tipo inteiro
print(np.zeros(10, dtype=int))
print('')

#Criar arrays com 8 elementos iguais a 12, tipo flutuante
print(np.full(8,12, dtype=float))
#Array tridimensional 

import numpy as np

#array tridimensional (lista de três dimensões)
# Cada colchete aninhado representa uma dimensão do array 

cubo = np.array([ [[1,4,7],[3,5,2]], [[5,6,0],[7,4,1]], [[2,8,8], [0,3,6]] ])
print("Array tridimensional:\n", cubo)



#Visualizar elementos especificos do cubo
print('\nItem na posição 0,0,0:', cubo[0,0,0])
print('\nItem na posição 1,0,0:', cubo[1,0,0])
print('\nItem na posição 2,0,0:', cubo[2,0,0])

#Número de dimensões do array

print('Número de dimensões do array cubo:', cubo.ndim)

#Dimensões do array
print('Tamanho do array cubo:', cubo.shape)

#Número total de elementos do array
print('Total de elementos do array cubo:', cubo.size)
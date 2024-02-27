#Criação de arrays com Numpy
#instalar o numpy via:   pip install numpy 


import numpy as np

numeros = np.array([2,6,7,9,0,1,2,5,6], np.int16)
print(type(numeros))
print(numeros)



#Array bidimensional com Numpy
M = np.array([[1,3,5],[2,4,6],[3,5,7]])
print(M)


#Visualizar uma coluna inteira 
print('Primeira coluna',M[:,0])
print('Segunda coluna',M[:,1])
print('Terceira coluna',M[:,2])


#visualizar uma linha inteira
print('Segunda Linha', M[1,:])



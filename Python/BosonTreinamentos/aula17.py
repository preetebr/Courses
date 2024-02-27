L = []
print(L)
L =[0,1,2,3,4]
print(L)
L = ["a", 'b', 'c']
print(L)
L = ['a' , ['b' , 'c', 'd']]
print(L)

L2 = [5 ,6 , 7 ,8]
print(L2)
list = ( L + L2)
print(list)

print(L2 * 2 )

for x in L2:
    print(x)

L2 = [5 ,6 , 7 ,8]
# L2.sort() #Ordena a lista
# print(L2)

# L2.reverse() #rever a ordem da lista
# print(L2)

# L2.remove(x) #remove a primeira ocorrência da lista
# print(L2)

# L2.pop(1) #remove item na posição especificada
# print(L2)

# del L2[1] #remove item na posição espeficada 
# print(L2)

# del L2[1:2] #remove os itens das posições 1 até 2 podendo ser usado tambem [i:j] removendo de I até J 
# print(L2)

#L[2] = 14 #Atribuição de valor a posição 1
#print(L)


print(len(L2))
print(map(1,L2))

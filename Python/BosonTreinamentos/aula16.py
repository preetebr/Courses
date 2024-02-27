#Listas 

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

L2.append(10)
print(L2)

L2.insert(2, 11)
print(L2)

y = L2.index(8)
print(y)

x = L2.count(5)
print(x)


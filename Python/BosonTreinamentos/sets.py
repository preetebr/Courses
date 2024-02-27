planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)

qtde_p = len(planeta_anao)
print(qtde_p)

'Ceres' in planeta_anao

for astro in planeta_anao:
    print(astro.upper())

astros = ['Lua', 'Venus', 'Sirius', 'Marte', 'Lua']
print('Listas:', astros)
astrosSet = set(astros)
print('Conjunto: ', astrosSet)

p1 = {'Terra', 'Venus', 'Mercurio', 'Marte'}
p2 = {'Terra', 'Venus', 'Mercurio', 'Marte', 'Saturno'}
print(p1 == p2)
print(p1 != p2) #Diferente 

p1 = {'Terra', 'Venus', 'Mercurio', 'Marte', 'Netuno'}
p2 = {'Terra', 'Jupiter', 'Urano', 'Marte', 'Saturno'}
p3 = {'Jupiter', 'Urano', 'Saturno'}
p1.add('Jupiter')
p1.remove("Terra")
uniao = p1 | p2
print(uniao)
print(p1.union(p2))

print( p1 & p2) #intersecção 
print(p1.intersection(p2))
print(p2.difference(p1))
print(p1 ^ p2) #simétrica
print(p1.symmetric_difference(p2))
print(p1.isdisjoint(p3)) #elementos em comum
p4 = p1.copy()
print('P1: ', p1)
print('P4: ', p4)
print(p1.pop())
print(p1.clear())





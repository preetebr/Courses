D = {'b':2, 'a':1, 'd':4, 'c':3}
#ordenada = list(D.keys())
#ordenada.sort()

#or key in ordenada:
#    print(key, '=', D[key])

for key in sorted(D):
    print(key, '=', D[key])
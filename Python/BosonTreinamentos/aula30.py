import random

print("Gerando números aleatórios: ")
for i in range(1,6):
    n = random.randint(1,50)
    print("Numero gerado: ", n)



print("Gerando números aleatórios flutuantes: ")
for it in range(1,6):
    num = random.random()
    print("Numero gerado: ", num * 10)


for iti in range(1,6):
    nume = random.uniform(1,100)
    print("Numero gerado: ", nume)


L = [2,4,6,8,10,12,14,16,18,20]
print("Gerando número aleatório da lista: ")
#n = random.choice(L)
# n = random.sample(L, 3)
n = random.shuffle(L)
print("Número gerado: ", n)
import random
def parimpar(num):
    if num%2==0:
        return 'par'
    else:
        return 'impar'

lista=[]
for i in range(10):
    lista.append(round(random.randrange(100)))
print(lista)
for i in lista:
    print(i)
   
    print(parimpar(i))

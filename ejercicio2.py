import random
num=random.randint(10,25)
lista=[]
for a in range(num):
    lista.append(round(random.random()*100))
print("lista: ",lista)
for a in lista:
    i=1
    cont=0
    while(a>=i):
        if a%i==0:
            cont+=1
        i+=1
    if not cont>2 or a <=1:
        print("el numero ",a," es primo")


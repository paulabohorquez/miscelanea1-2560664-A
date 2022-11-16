import random 
tam=random.randint(10,25)
vector=[round(random.random()*100)for i in range(tam)]
print("la lista sin ordenar es: ", vector)
a=True
while a:
    a=False
    for i in range(len(vector)-1):
        if vector[i]>vector[i+1]:
            vector[i],vector[i+1]=vector[i+1],vector[i]
            a=True
print("lista ordenada: ", vector)
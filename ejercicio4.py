import random 
vector=[]
tam=random.randint(10,25)
for i in range(tam):
    vector.append(round(random.random()*100))
print("la lista sin ordenar es: ", vector)
a=True
while a:
    a=False
    for i in range(len(vector)-1):
        if vector[i]>vector[i+1]:
            vector[i],vector[i+1]=vector[i+1],vector[i]
            a=True
print("lista ordenada: ", vector)
import random
veccant=[]
tam=random.randint(10,25)
vector=[round(random.random()*100)for i in range(tam)]
print("lista: ", vector)
contador=0
for i in range(len(vector)):
    contador=0
    for j in vector:
        if vector[i]==j:
            
    if contador!=0:
        veccant.append(contador)
    else:
        veccant.apend(0)
print(vector)
print(veccant)
mayor=0
pos=0
for i in range(len(vector)):
    if mayor<veccant[i]:
        mayor=veccant[i]
print("el mayor es: ", mayor)
for j in range (len(veccant)):
    if mayor==veccant[j]:
        print("la moda es: ", vector[j])
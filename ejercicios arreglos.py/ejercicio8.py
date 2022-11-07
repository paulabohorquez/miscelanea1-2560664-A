import random
vector=[]
veccant=[]
tam=random.randint(10,25)
for i in range(tam):
    vector.append(round(random.random()*100))
print(vector)
contador=0
for i in range(len(vector)):
    contador=0
    for j in vector:
        if vector[i]==j:
            contador+=1
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
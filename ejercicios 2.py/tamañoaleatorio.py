import random


tam=random.randint(10,25)
vector=[]
suma=0
contador=0
for i in range(tam):
    vector.append(round(random.random()*100))
print(vector)
for i in range(tam):
    suma+=vector[i]
    contador+=1
    p = suma//contador
print(suma)
print(p)
    



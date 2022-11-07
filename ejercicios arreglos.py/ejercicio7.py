import random
vector=[]
suma=0
promedio=0
tam=random.randint(10,25)
for i in range(tam):
    vector.append(round(random.random()*100))
    suma+=vector[i]
    promedio=suma//tam
print("rango lista:", tam)
print("elementos de la lista: ", vector)
print("suma: ", suma)
print("promedio: ",promedio)
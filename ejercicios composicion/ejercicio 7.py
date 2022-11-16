import random
suma=0
promedio=0
tam=random.randint(10,25)
vector=[round(random.random()*100)for i in range(tam)]
for i in range(tam):
    suma+=vector[i] 
    promedio=suma//tam
print("rango lista:", tam)
print("elementos de la lista: ", vector)
print("suma: ", suma)
print("promedio: ",promedio)

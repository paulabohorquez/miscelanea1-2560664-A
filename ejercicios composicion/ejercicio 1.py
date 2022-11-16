import random
promedio=0
suma=0
tam=random.randint(10,25)
vector=[round(random.random()*100)for i in range(tam)]
for i in range(tam):
    suma+=vector[i]
print("suma: ",suma)
promedio=suma//tam
print("rango: ",tam)
print("valores de lista: ",vector)
print("promedio: ",promedio)
for x in vector:
    if x<promedio:
        print("el numero",x," es menor al promedio")
    elif x>promedio:
        print("el numero",x," es mayor al promedio")
    elif x==promedio:
        print("el numero ",x," es igual al promedio")
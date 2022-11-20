import random
lista=[]
tam=random.randint(10,25)
for i in range(tam):
    lista.append(round(random.random()*100))
def suma(lista):
    suma=0
    promedio=0
    for i in range(tam):
        suma+=lista[i]
        promedio=suma//tam
    return suma,promedio


print("rango lista: ",tam)
print("elementos de la lista: ", lista)
print("suma: ", suma)
print("promedio: ", promedio)






lista=[]

'''for i in range(10):
    lista.append(round(random.randrange(100)))
print(lista)
for i in lista:
    print(i)'''
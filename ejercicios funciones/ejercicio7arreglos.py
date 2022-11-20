import random
def tamañolista(lista):
    tam=round(random.randrange(10,25))
    for i in range(tam):
        lista.append(round(random.randrange(100)))
    lista.sort()
    return lista
    

def mediana(lista):
    mitad=(len(lista)//2)
    if mitad%2==0:
        me=(lista[mitad-1]+lista[mitad])//2
    else:
        me=lista[mitad]
    return me
        
lista=[]   
lista.sort()

print("lista ordenada: ", tamañolista(lista))
print("la longitud del vector es: ",len(lista))
print("la mediana del vector es: ", mediana(lista))
        




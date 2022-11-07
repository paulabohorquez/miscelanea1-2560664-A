import random
vector=[]
tam=random.randint(10,25)
for i in range(tam):
    vector.append(round(random.random()*100))
print("lista ordenada: ", vector)
vector.sort()
print("lista ordenada: ",vector)
mitad=int(tam//2)

if tam %2==0:
    mediana=(vector[mitad-1]+vector[mitad])//2
else:
    mediana=vector[mitad]
print("la longitud del vector es: ", tam)
print("la mediana del vector es: ", mediana)
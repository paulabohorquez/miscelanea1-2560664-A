import random
par=0
impar=0
promedio=0
contador=0
vector=[]
tam=random.randint(10,25)
vector=[]
for i in range(tam):
    vector.append(round(random.random()*100))
for i in range(tam):
    if vector[i]%2==0:
        par+=vector[i]
    else:
        impar+=vector[i]
        contador+=1
        promedio=impar//contador
print("la longitud de la lista es: ",tam," y los valorea de la lista son:", vector)
print("la suma de los pares es: ",par)
print("el promedio del impar es: ", impar)
   
    


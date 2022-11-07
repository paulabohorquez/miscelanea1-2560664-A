import random
vector=[]
tam=random.randint(10,25)
contador=0
posicion=" "
for i in range(tam):
    vector.append(round(random.random()*100))
print(vector)
num=int(input("escribe un numero: "))
for i in range(tam):
    if num==vector[i]:
        posicion+=str(i)+" "
        contador+=1
if contador==0:
    vector.append(num)
    print("el numero se agrego al final de la lista")
    print(vector)
else:
    if contador==1:
        print("el numero de la lista ",num," esta 1 vez en la posicion ", posicion)
    else:
        print("el numero de la lista ",num," esta ",contador," veces y esta en las posiciones", posicion)
import random
tam=random.randint(10,25)
vector=[round(random.random()*100)for i in range(tam) ]
vector.sort()
print("lista ordenada: ", vector)
mitad=int(tam//2)
if tam %2==0:
    mediana=(vector[mitad-1]+vector[mitad])//2
else:
    mediana=vector[mitad]
print("longitud del vector:", tam)
print("mediana: ",mediana)






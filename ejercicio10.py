import random
random1=[]
tam=random.randint(10,25)
suma=0
promedio=0
contador=0
desviacion=0
tamaño2=0
for i in range(tam):
    random1.append(round(random.random()*100))
    suma+= random1[i]
    contador+=1
    promedio=suma//contador
    random1.sort()
    tamaño=len(random1)
    tamaño2=tamaño-1
    desviacion=(suma-promedio)**2
    dividir=desviacion//tamaño2
    resultadofinal=dividir**0.5
    print("la lista es: ", random1)  
    print("desviacion estandar: ", resultadofinal)  
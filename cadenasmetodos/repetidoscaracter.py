#cuantas veces se repite un carecter dado
def caracter(c):
   
    lista1=[]
    lista2=[]

    for i in c:
        if i not in lista1:
            lista1.append(i)
        else:
            if i in lista1:
                lista2.append(i)
    print('hay: ', len(lista2), 'letras repetidas')
        


print(caracter('hoooolaaaaa'))
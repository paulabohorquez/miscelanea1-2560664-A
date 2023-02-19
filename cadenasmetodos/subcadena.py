#Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras,
#luego tres primeras y así sucesivamente hasta llegar a la última

def cadena(c):
    cadena2=''
    for i in c:
        cadena2+=i
        print('cadena:', cadena2)

cadena('moijerigjgm')
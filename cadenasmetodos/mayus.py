#Solicite cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas
def palabra():
    pal=input('ingrese palabra: ')
    return 'formas posibles', pal.lower(), pal.upper(), pal.swapcase(), pal.title()
  
print(palabra())

    

    
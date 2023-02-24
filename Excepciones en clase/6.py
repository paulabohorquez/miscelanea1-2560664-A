#TypeError: se produce cuando se intenta realizar una operación con un tipo de datos inadecuado.
def ErrordeTipo(a,b): #se crea una funcion con dos parametros
    try:
        c = a/b #en c queda el resultado de la division
    except TypeError: 
        print("TypeError: Error en los tipos de datos") #se imprime el tipo de error 

    else:
        print(f'el resultado de la division es: {c}') #se crea el else por si no se cumple el except anterior 
    
ErrordeTipo('a',2) #se invoca la funcion y se agregan dos argumentos 
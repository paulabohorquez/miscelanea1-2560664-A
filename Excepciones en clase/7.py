#OverflowError: Se produce cuando un cálculo númerico produce un resultado que es demsiado grande para ser representado.
def overflowerror(a,b):  #se crea una funcion con dos parametros
    try:
        resultado=a**b #en resultado queda la operacion realizada
    except OverflowError:
        print("OverflowError: no se puede realizar la operacion") #se imprime si sucede el error 
    else:
        print(f'el resultado es: {resultado}') #se imprime si se cumple


overflowerror(25.6,2) #se invoca la funcion y se agregan los parametros 
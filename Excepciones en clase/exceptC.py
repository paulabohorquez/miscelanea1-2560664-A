def try_syntax(numerator, denominator): #se crea una funcion con dos parametros
    try:
        result = numerator / denominator # se agrega a la variable la operacion realizada
        print(f'In the try block: {numerator}/{denominator}/ y el resultado de la operacion es: {result}')  #se imprime los dos argumentos ingresados en la funcion
        #quiero ver el resultado de la operacion en el print
        
    except ZeroDivisionError as zde: #se le asigna zde al error 
        print(zde) #see imprimira el error
    else:
        print('The result is:', result) #se imprimira el resultado
        return result #retornara el resultado de la operacion
    finally:
        print('Exiting')# se imprimira al final del programa 
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 5))

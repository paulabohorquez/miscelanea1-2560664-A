try: # se crea el try para el bloque de codigo
    #raise ZeroDivisionError, ponemos raise para generar este tipo de error 
    print(1/0) #se imprimira la division
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde: # se le asigna a zde el error
    print(zde) #se imprime 
    #print('prueba error')
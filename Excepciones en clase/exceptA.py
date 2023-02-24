#en la linea dos hay un try que es un bloque de codigo en el cual se realiza una accion y si llega a salir mal tomara lo que halla en los except,
#en el try hay un print que tiene un error de sintaxix
try:
    #print(1/1))
    raise SyntaxError #en esta linea se genera el error
except SyntaxError as e: #aqui se le asigna syntaxerror a la letra e 
    print(e) #se imprime la e
    print('Cierra el parentesis') #si el error corresponde a este se imprimira
    
try:
    #raise ZeroDivisionError   
    print(1/0) #se esta imprimiendo una operacion
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde: #se le asigna el nombre al error
    print(zde) #se imprime 
    #print('prueba error')
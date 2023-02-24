def edad(): #se crea una funcion sin parametros
    try: #ponemos el try para crear el bloque de codigo
        tuedad=int(input("introduce tu edad")) #se crea un input para ingresar la edad, que solo soporta vvalores numericos 
        print(f'tu edad es  {tuedad}') #se imprime la edad ingresada
        #print('Tu edad es ',tuedad)
    except ValueError as e:    #en el excepto se le asigna a la letra ValueError
        print(e) #se imprimira el nombre del error 
        print("La edad debe ser un valor numerico...") #se imprimira este mensaje indicando que se reciben valores numericos 
        edad() #se invoca a la misma funcion dentro de ella para que se repita hasta que la edad sea valor numerico
    
edad() #se invoca la funcion
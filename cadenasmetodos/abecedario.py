def funcion( ):
    cadena="lopayyttts"
    l=[]
    tamano=(len(cadena))

    for i in cadena:
        if i not in l:
            l.append(i)
    tamano2=len(l)
    print('cadena', l)
    print("la cadena tiene",tamano,"letras")
    print("la cadena sin repetir letras tiene",tamano2,"letras")
    
    
funcion()
#Pida una cadena por teclado y diga cual es el valor numerico de acuerdo a los códigos del alfabetocual y su valor al sumar sus codigos

def codigo(cad):
    codigos=[]
    b=0
    for l in cad:
        codigos.append(ord(l))
        print('la letra es',l, 'y su codigo es', ord(l))
    print('la suma de los codigos es:',sum(codigos))
        
c=input('ingrese los caracteres: ')  
codigo(c)

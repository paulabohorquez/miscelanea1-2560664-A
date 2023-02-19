def cifrado():
    cadena = input("Ingresa tu mensaje: ")
    lista=[]
    cad = ''
    for i in cadena:
        lista.append(ord(i))
        i= i.upper()
        j = ord(i) + 2
        if j > ord('Z'):
            j = ord('A')
        cad += chr(j)
    print('el mensaje en letras es: ',cad, 'el mensaje e numeros es: ',lista)
cifrado()

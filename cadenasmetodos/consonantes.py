def vocales(v):
    cont=0
    cont1=0
    cont2=0
    cont3=0
    for letra in v:
        if letra in 'aeiou':
            cont+=1
        if letra in 'bcdfghjklmnñpqrstvwxyz':
            cont1+=1
        if letra in 'áéíóú':
            cont2+=1
        if letra in '+-*/:;¿?¡1$%_#.,':
            cont3=1
    return ('las vocales son:',cont, 'las consonantes son: ',cont1, 'las tildes son: ',cont2, 'los caracteres especiales son: ',cont3)
print(vocales('corazón#'))



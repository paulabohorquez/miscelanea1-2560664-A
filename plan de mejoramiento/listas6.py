#, construiremos una lista vacia e iremos añadiendo numeros primos conforme 
#los vayamos encontrando.
n=int(input("introduce numero: "))
primos = []
for i in range(1, n+1):
    creo_que_es_primo = True
    for divisor in range(2, n):
        if n % divisor == 0:
            creo_que_es_primo = False
            break
    if creo_que_es_primo:
        primos.append(i)

print(primos)

def perfecto():
   for a in range(1,1000):
    i=1
    contador=0
    while(a > i):
     if a%i ==0:
        contador+=i
     i+=1
    if a == contador:
       print("el numero ",a," es perfecto")
perfecto()
values = (1, 0) #en esta linea se crea una tupla
#x,y=10,12   aqui se le asigna un valor a cada letra 
#print(divmod(10,3))   se imprime una division con su cociente y residuo
try:
    q, r = divmod(*values) #se realiza una division a la tupla y para independizar cada valor ponemos un asterisco 


    #print('valor de q=',q)
    print(f'q={q}') #se imprime el valor de la division, ponemos la letra f para poder poner todo sobre comillas y el valor que desea imprimir se pondra en los corchetes 
    print(f'r={r}') #se imprime el valor de la division, ponemos la letra f para poder poner todo sobre comillas y el valor que desea imprimir se pondra en los corchetes 
except (ZeroDivisionError, TypeError) as e:  #se le asigna a e los dos errores en parentesis
    print(type(e), e) #el type mira que error se esta generando e imprime el correcto
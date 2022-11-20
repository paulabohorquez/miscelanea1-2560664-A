import random
def fibonacci(num):
    d=True
    a=0
    b=1
    c=1
    while d:
        if num>=5 and num<=20:
            d=False
        else:
            print("minimo 5 elementos y maximo 20")
    for i in range(num):
        c=a+b
        a=b
        b=c
        lista.append(c)
lista=[]
fibonacci(6)
print("numero serie de fibonacci son: ", lista)
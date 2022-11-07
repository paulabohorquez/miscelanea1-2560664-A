a=int(input("ingrese la base: "))
b=int(input("ingrese el exponente: "))
i=1
c=a
while(i<b):
    i+=1
    c*=a
if b<=0:
    c=1
print(c)

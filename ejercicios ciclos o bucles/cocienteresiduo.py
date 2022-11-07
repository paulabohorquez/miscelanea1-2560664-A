from pickle import BINFLOAT


a = int(input("ingrese el rimer numero: "))
b = int(input("ingrese el segundo numero: "))
while not (b == 0):
    c=a
    d=b
    if a < 0:
        a=-c
        b=d
    if b < 0:
        a=c
        b=-d
    else:
        a= d
        b= c%d
print(a)
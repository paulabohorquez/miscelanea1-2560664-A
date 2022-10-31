i=1
a = 0
b = 0
c = int(input("ingrese numero: "))
while(c > i):
 if c%i ==0:
  a=i
 i+=1
for i in range(a +1):
 b+=1
if c == b:
 print("el numero ",c," es perfecto")
else:
 print("el numero ",c," no es perfecto")
 



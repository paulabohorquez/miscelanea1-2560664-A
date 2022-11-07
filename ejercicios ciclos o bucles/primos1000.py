for a in range(2,1000):
    i=1
    b = 0
    while(a >= 1):
     if a%i ==0:
      b+=1
     i+=1
     if not b > 2 or a <=1:
      print("el numero ",a," es primo")
       
a = 0
for n in range (100, 1000):
    a = n
    u=n%10
    n=n//10
    d=n%10
    n=n//10
    c=n%10
    u**=3
    d**=3
    c**=3
    suma = u+d+c
    if suma == a:
        print(a)
def divisores(num):
    i = 1
    print("los divisores son: ")
    while(num >= i):
        if num%i == 0:
            print(i)
        i+=1
divisores(55)

def resultado(base,exponente):
   i=1
   c=base
   while(i<exponente):
    i+=1
    c*=base
    if exponente<=0:
        c=1
    print("resultado es",c)
resultado(4,5)

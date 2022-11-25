'''1. Se coloca un capital C, a un interés I (que oscila entre 0 y
100), durante M años y se desea saber en cuanto se habrá
convertido ese capital en “M” años, sabiendo que es
acumulativo.'''
c=-1
i=0
m=0
while (c<0) or (i<=0) or (i>=100) or (m<=0):
    print("introduce el capital, interes y el tiempo apropiados")
    c=int(input("capital: "))
    i=int(input("interes: "))
    m=int(input("tiempo en años: "))
for i in range(m):
    c=c*(1+1/100)
print("tienes",c, "soles")

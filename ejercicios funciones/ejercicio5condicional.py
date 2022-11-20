def llamada(num):
    c = (num * 50) + 200
    if num < 3:
        print("su llamada cuesta 200 pesos")
    elif num > 4:
        print("su llamada cuesta: ", c)

llamada(50)